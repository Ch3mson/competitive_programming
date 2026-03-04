"""
Part 1:
Implement a retry mechanism for a flaky external API. The solution should:

Use exponential backoff between retry attempts.
Include jitter in the delay to avoid synchronized retries.
Retry on timeouts and server-side errors (e.g., 5xx responses).
Avoid retrying on client-side errors (e.g., 4xx responses).
Enforce reasonable limits on the number of retries and/or total elapsed time.

Part 2:
You are given an e-commerce product catalog where some products have missing primary IDs but include a backup_id field that refers to another product. Implement logic to:

Recursively follow backup_id references to resolve and populate missing product IDs.
Detect and safely handle circular references in the backup_id chain so the process does not loop indefinitely.
Return the final list of products after resolution.
Filter out any products that are out of stock from the returned result.

Part 3:
Synchronize inventory across multiple warehouses with inconsistent field names. Implement conflict resolution rules based on the product timestamps.
"""

import time
import random
from typing import List, Dict, Optional
from collections import defaultdict


# Custom exception to simulate API timeouts
class MockTimeoutError(Exception):
    pass


def external_api_call(endpoint: str, mock_data: Optional[List[Dict]] = None) -> dict:
    """
    Simulates a flaky external API.
    """
    # simulate network latency
    time.sleep(random.uniform(0.05, 0.3))

    roll = random.random()

    # 15% timeout
    if roll < 0.15:
        raise MockTimeoutError("Request timed out")

    # 15% server error
    elif roll < 0.30:
        return {
            "status": random.choice([500, 502, 503, 504]),
            "data": None,
            "error": "Internal Server Error"
        }

    # 10% client error
    elif roll < 0.40:
        return {
            "status": random.choice([400, 401, 403, 404]),
            "data": None,
            "error": "Bad Request or Not Found"
        }

    # 60% success
    else:
        return {
            "status": 200,
            "data": {
                "endpoint": endpoint,
                "products": mock_data or []
            }
        }


# Part 1
def fetch_catalog(endpoint: str,
                  mock_data: Optional[List[Dict]] = None,
                  max_retries: int = 5,
                  base_delay: float = 0.5,
                  max_delay: float = 10.0,
                  timeout_seconds: float = 30.0) -> dict:
    """
    Implement exponential backoff with jitter here.
    """
    response = None
    start = time.time()
    for i in range(max_retries):
        try:
            response = external_api_call(endpoint, mock_data)
            if response and response["status"] == 200:
                break
            elif response and response["status"] < 600 and response["status"] >= 500:
                print(f'Error {response["status"]} on {i}th attempt')
            elif response and response["status"] >= 400 and  response["status"] < 500:
                # client side error
                print(f'Error {response["status"]} on {i}th attempt, breaking')
                break
            
        except MockTimeoutError:
            print(f"Some random error occured on {i}th attempt")

        if i < max_retries - 1:
            exponential_delay = base_delay * (2 ** i)
            delay = min(exponential_delay, max_delay)
            jitter = random.uniform(0, 0.1 * exponential_delay)
            if time.time() - start +  delay + jitter > timeout_seconds:
                break
            else:
                time.sleep(delay + jitter)

    return response



# Part 2
def resolve_product_ids(products: List[Dict]) -> List[Dict]:
    """
    Implement ID resolution, cycle detection, and filtering here.
    """
    visited = set()
    idToBackup = {}

    for product in products:
        if product["id"]:
            idToBackup[product["id"]] = product["backup_id"]

    def traverseProduct(product):
        if product in visited:
            return
        if product["id"]:
            return product["id"]

        visited.add(product)
        for p in products:
            if p["id"] == product["backup_id"]:
                visited.add(p)
                new_id = traverseProduct(p)
                if new_id:
                    product["id"] = new_id
        visited.remove(product)
    
    for product in products:
        traverseProduct(product)
    


    
        
        


# Part 3
def sync_inventory(warehouses: List[List[Dict]]) -> Dict[str, Dict]:
    """
    Implement cross-warehouse synchronization and conflict resolution here.
    """
    pass


# ---------------------------------------------------------
# Mock Data
# ---------------------------------------------------------

CATALOG_DATA = [
    # Root products
    {"id": "P100", "name": "Laptop Pro 16", "backup_id": None, "in_stock": True},
    {"id": "P101", "name": "Laptop Air 13", "backup_id": None, "in_stock": True},
    {"id": "P102", "name": "Wireless Mouse", "backup_id": None, "in_stock": True},
    {"id": "P103", "name": "Mechanical Keyboard", "backup_id": None, "in_stock": False}, # should be filtered
    {"id": "P104", "name": "4K Monitor", "backup_id": None, "in_stock": True},

    # Single-level backup chains
    {"id": None, "name": "Laptop Pro 16 Refurbished", "backup_id": "P100", "in_stock": True},
    {"id": None, "name": "Laptop Air 13 Open Box", "backup_id": "P101", "in_stock": True},
    {"id": None, "name": "Mouse Special Edition", "backup_id": "P102", "in_stock": True},

    # Multi-level backup chains
    {"id": None, "name": "Laptop Pro Legacy", "backup_id": "P200", "in_stock": True},
    {"id": "P200", "name": "Laptop Pro Old Gen", "backup_id": None, "in_stock": True},
    {"id": None, "name": "Laptop Pro Very Old", "backup_id": "P300", "in_stock": True},
    {"id": "P300", "name": "Laptop Pro Ancient", "backup_id": None, "in_stock": True},

    # Chain length 3
    {"id": None, "name": "Keyboard Legacy", "backup_id": "P400", "in_stock": True},
    {"id": None, "name": "Keyboard Legacy Intermediate", "backup_id": "P401", "in_stock": True},
    {"id": "P401", "name": "Keyboard Legacy Root", "backup_id": None, "in_stock": True},
    {"id": None, "name": "Keyboard Legacy Broken Link", "backup_id": "P999", "in_stock": True},

    # Circular references
    {"id": None, "name": "Circular Product A", "backup_id": "CIRC2", "in_stock": True},
    {"id": "CIRC2", "name": "Circular Product B", "backup_id": "CIRC3", "in_stock": True},
    {"id": "CIRC3", "name": "Circular Product C", "backup_id": "CIRC2", "in_stock": True},

    # Broken references (no valid root)
    {"id": None, "name": "Ghost Product", "backup_id": "NONEXISTENT", "in_stock": True},

    # Out of stock but with valid backup
    {"id": None, "name": "Monitor Refurbished", "backup_id": "P104", "in_stock": False}, # should be filtered

    # Valid products deeper in list
    {"id": "P500", "name": "USB-C Hub", "backup_id": None, "in_stock": True},
    {"id": None, "name": "USB-C Hub Variant", "backup_id": "P500", "in_stock": True},

    # Multiple products referencing same backup
    {"id": None, "name": "Mouse Variant A", "backup_id": "P102", "in_stock": True},
    {"id": None, "name": "Mouse Variant B", "backup_id": "P102", "in_stock": True},

    # Self reference cycle
    {"id": "SELF1", "name": "Self Cycle Product", "backup_id": "SELF1", "in_stock": True},

    # Long valid chain
    {"id": None, "name": "Chain Level 1", "backup_id": "CHAIN2", "in_stock": True},
    {"id": None, "name": "Chain Level 2", "backup_id": "CHAIN3", "in_stock": True},
    {"id": "CHAIN3", "name": "Chain Root", "backup_id": None, "in_stock": True},

    # Another broken chain
    {"id": None, "name": "Broken Chain Level 1", "backup_id": "BROKEN2", "in_stock": True},
    {"id": None, "name": "Broken Chain Level 2", "backup_id": "BROKEN3", "in_stock": True},
]


# Example driver
def main():
    print("--- Testing Part 1: Fetching Catalog ---")
    # You might want to wrap this in a try/except in case your retry limits are exceeded
    response = fetch_catalog("/api/v1/products", mock_data=CATALOG_DATA)
    
    if not response or response.get("status") != 200:
        print(f"Failed to fetch catalog. Final response: {response}")
        return

    fetched_products = response["data"]["products"]
    print(f"Successfully fetched {len(fetched_products)} raw products.\n")

    print("--- Testing Part 2: Resolving IDs ---")
    resolved_products = resolve_product_ids(fetched_products)
    
    # Simple check to see how many made it through your logic
    if resolved_products:
        print(f"Resolved {len(resolved_products)} valid, in-stock products.")
        # print(resolved_products) # Uncomment to see the final list
    else:
        print("No products returned from resolve_product_ids.")


if __name__ == "__main__":
    main()