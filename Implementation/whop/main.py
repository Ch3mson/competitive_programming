import json
from typing import Iterator, Dict, Any
from difflib import SequenceMatcher
import sqlite3

"""
Todo:

1. load receipt and transsaction jsons
2. users.db:

    users.id <- spend_allocation_mapping.user_id <- card.id

Relationships:
Users must OWN that card from 

Relate transactions.card_token with cards owned by receipts.user_id
"""

def load_card_to_user_mapping(db_path: str) -> Dict[str, str]:
    """
    Load mapping of card_token -> user_id
    
    Query joins: cards -> spend_allocation_mapping -> users
    Returns: {card_token: user_id}
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Join tables to get card token to user mapping
    query = """
    SELECT c.token, sam.user_id
    FROM cards c
    JOIN spend_allocation_mapping sam ON c.id = sam.card_id
    """
    
    cursor.execute(query)
    mapping = {token: user_id for token, user_id in cursor.fetchall()}
    
    conn.close()
    return mapping


def read_jsonl(filepath: str) -> list[Dict[str, Any]]:
    """Read JSONL file and return list of records"""
    records = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                records.append(json.loads(line))
    return records

def fuzzy_match_merchant(txn_merchant: str, receipt_merchant: str | None) -> int:
    """
    Compare merchant names and return score 0-30.
    Handles processor prefixes like "SQ *" and partial matches.
    """
    if not receipt_merchant:
        return 0  # Can't match if receipt has no merchant
    
    # Normalize: uppercase, remove common prefixes
    txn_clean = txn_merchant.upper().strip()
    receipt_clean = receipt_merchant.upper().strip()
    
    # Remove common payment processor prefixes
    prefixes = ['SQ *', 'TST*', 'PAYPAL *', 'STRIPE *']
    for prefix in prefixes:
        if txn_clean.startswith(prefix):
            txn_clean = txn_clean[len(prefix):].strip()
    
    # Exact match after cleaning
    if txn_clean == receipt_clean:
        return 30
    
    # Check if one contains the other
    if txn_clean in receipt_clean or receipt_clean in txn_clean:
        return 25
    
    # Use sequence matcher for similarity ratio
    similarity = SequenceMatcher(None, txn_clean, receipt_clean).ratio()
    
    if similarity > 0.8:
        return 20
    elif similarity > 0.6:
        return 15
    elif similarity > 0.4:
        return 10
    else:
        return 0

def calculate_match_score(txn, receipt, user_match):
    if not user_match:
        return 0 
    
    score = 0
    
    # Amount similarity (40 points)
    amount_diff = abs(txn['amount'] - receipt['extracted_data']['total_amount'])
    if amount_diff < 0.01:
        score += 40
    elif amount_diff < 0.50:
        score += 30
    elif amount_diff < 2.00:
        score += 20
    
    # Timestamp proximity (30 points)
    time_diff = abs(txn['timestamp'] - receipt['timestamp'])
    if time_diff < 300:  # 5 minutes
        score += 30
    elif time_diff < 3600:  # 1 hour
        score += 20
    elif time_diff < 86400:  # 1 day
        score += 10
    
    # Merchant similarity (30 points)
    merchant_score = fuzzy_match_merchant(
        txn['card_acceptor']['name'],
        receipt['extracted_data'].get('merchant_name')
    )
    score += merchant_score
    
    return score

if __name__ == "__main__":
    print("=" * 60)
    print("RECEIPT MATCHER - MVP")
    print("=" * 60)
    
    # Load database mapping
    print("\n[1] Loading card-to-user mapping from database...")
    card_to_user = load_card_to_user_mapping('users.db')
    print(f"    Loaded {len(card_to_user)} card-to-user mappings")
    
    # Load data files
    print("\n[2] Loading transactions...")
    transactions = read_jsonl('transactions.jsonl')
    print(f"    Loaded {len(transactions)} transactions")
    
    print("\n[3] Loading receipts...")
    receipts = read_jsonl('receipts.jsonl')
    print(f"    Loaded {len(receipts)} receipts")
    
    # Simple matching approach: try to match each receipt to transactions
    print("\n[4] Matching receipts to transactions...")
    print("-" * 60)
    
    matches = []
    unmatched_receipts = []
    
    MATCH_THRESHOLD = 70  # Minimum score to consider a match
    
    for receipt in receipts:
        receipt_user = receipt.get('user_id')
        receipt_amount = receipt['extracted_data']['total_amount']
        receipt_merchant = receipt['extracted_data'].get('merchant_name', 'Unknown')
        
        best_match = None
        best_score = 0
        
        # Search for matching transaction
        for txn in transactions:
            # Get user for this transaction
            txn_user = card_to_user.get(txn.get('card_token'))
            user_match = (txn_user == receipt_user)
            
            # Calculate match score
            score = calculate_match_score(txn, receipt, user_match)
            
            if score > best_score:
                best_score = score
                best_match = txn
        
        # Record match if score is high enough
        if best_score >= MATCH_THRESHOLD:
            matches.append({
                'receipt_id': receipt['id'],
                'transaction_id': best_match['id'],
                'score': best_score,
                'timestamp': receipt['timestamp'],  # Match timestamp
                'amount': receipt_amount,
                'merchant': receipt_merchant
            })
        else:
            unmatched_receipts.append(receipt)
    
    # Display results
    print(f"\n{'='*60}")
    print(f"RESULTS")
    print(f"{'='*60}")
    print(f"Total receipts:           {len(receipts)}")
    print(f"Matched:                  {len(matches)}")
    print(f"Unmatched:                {len(unmatched_receipts)}")
    print(f"Match rate:               {len(matches)/len(receipts)*100:.1f}%")
    
    # Show first 10 matches
    print(f"\n{'='*60}")
    print(f"SAMPLE MATCHES (first 10)")
    print(f"{'='*60}")
    for i, match in enumerate(matches[:10], 1):
        print(f"\n[{i}] Match (score: {match['score']})")
        print(f"    Receipt:     {match['receipt_id'][:16]}...")
        print(f"    Transaction: {match['transaction_id'][:16]}...")
        print(f"    Amount:      ${match['amount']:.2f}")
        print(f"    Merchant:    {match['merchant']}")
        print(f"    Timestamp:   {match['timestamp']}")
    
    # Show some unmatched if any
    if unmatched_receipts:
        print(f"\n{'='*60}")
        print(f"SAMPLE UNMATCHED RECEIPTS (first 5)")
        print(f"{'='*60}")
        for i, receipt in enumerate(unmatched_receipts[:5], 1):
            print(f"\n[{i}] Unmatched Receipt")
            print(f"    ID:        {receipt['id'][:16]}...")
            print(f"    User:      {receipt['user_id'][:16]}...")
            print(f"    Amount:    ${receipt['extracted_data']['total_amount']:.2f}")
            print(f"    Merchant:  {receipt['extracted_data'].get('merchant_name', 'Unknown')}")
            print(f"    Timestamp: {receipt['timestamp']}")
    
    print(f"\n{'='*60}")
    print("DONE")
    print(f"{'='*60}\n")