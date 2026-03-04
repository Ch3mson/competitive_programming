"""
Fetching Products Challenge - Practice Starter

Tasks:
1. Implement get_products() - fetch, filter, sort, and select specific fields
2. Implement fetch_with_retry() - wrap network calls with retry logic
3. Implement get_all_similar_products() - recursively get all similar product IDs (DFS)

Run tests: python fetching_products2.py
"""

import json
import random
from typing import List, Dict, Any, Optional, Set


# Simulated network fetch (DO NOT MODIFY)
def _simulate_network_fetch(filepath: str) -> Dict:
    """
    Simulates a flaky network call that sometimes fails.
    In real scenario, this would be an HTTP request.
    """
    if random.random() < 0.3:  # 30% chance of failure
        raise ConnectionError("Network request failed")

    with open(filepath, 'r') as f:
        return json.load(f)


# ============================================================
# TASK 1: Get Products with filtering, sorting, and field selection
# ============================================================
def get_products(
    products: List[Dict],
    sort_by: Optional[str] = None,
    sort_order: str = "asc",
    filter_by: Optional[Dict[str, Any]] = None,
    fields: Optional[List[str]] = None
) -> List[Dict]:
    """
    Process a list of products with optional filtering, sorting, and field selection.

    Args:
        products: List of product dictionaries
        sort_by: Field name to sort by (e.g., "price", "name")
        sort_order: "asc" or "desc"
        filter_by: Dict of field->value to filter (e.g., {"category": "electronics", "in_stock": True})
        fields: List of fields to include in output (e.g., ["id", "name", "price"])

    Returns:
        Processed list of products

    Example:
        get_products(products, sort_by="price", sort_order="desc",
                     filter_by={"in_stock": True}, fields=["id", "name", "price"])
    """
    # TODO: Implement this function
    pass


# ============================================================
# TASK 2: Fetch with retry logic
# ============================================================
def fetch_with_retry(
    filepath: str,
    max_retries: int = 3,
    backoff_factor: float = 1.0
) -> Dict:
    """
    Fetch data with retry logic for handling network failures.

    Args:
        filepath: Path to the JSON file (simulating an API endpoint)
        max_retries: Maximum number of retry attempts
        backoff_factor: Multiplier for exponential backoff (optional to implement)

    Returns:
        The fetched data as a dictionary

    Raises:
        ConnectionError: If all retries are exhausted

    Hint: Use _simulate_network_fetch() which has a 30% failure rate
    """
    # TODO: Implement this function
    pass


# ============================================================
# TASK 3: Recursively get all similar products (DFS)
# ============================================================
def get_all_similar_products(
    product_id: str,
    products_map: Dict[str, Dict],
    max_depth: Optional[int] = None
) -> Set[str]:
    """
    Recursively find all similar products using DFS traversal.

    Args:
        product_id: Starting product ID
        products_map: Dict mapping product ID -> product dict
        max_depth: Optional maximum recursion depth (None = unlimited)

    Returns:
        Set of all similar product IDs (excluding the starting product)

    Example:
        If p001 -> [p002, p003] and p002 -> [p004]
        get_all_similar_products("p001", products_map) returns {"p002", "p003", "p004"}

    Note: Handle cycles! Products can reference each other.
    """
    # TODO: Implement this function
    pass


# ============================================================
# Helper function to build products map
# ============================================================
def build_products_map(products: List[Dict]) -> Dict[str, Dict]:
    """Convert list of products to a dict keyed by product ID."""
    return {p["id"]: p for p in products}


# ============================================================
# TESTS - Run to verify your implementation
# ============================================================
def run_tests():
    # Load test data
    with open("Implementation/products.json", "r") as f:
        data = json.load(f)
    products = data["products"]
    products_map = build_products_map(products)

    print("=" * 60)
    print("TASK 1: get_products() tests")
    print("=" * 60)

    # Test 1.1: Filter by category
    result = get_products(products, filter_by={"category": "electronics"})
    expected_count = 4
    if result and len(result) == expected_count:
        print(f"✓ Filter by category: Found {len(result)} electronics products")
    else:
        print(f"✗ Filter by category: Expected {expected_count}, got {len(result) if result else 'None'}")

    # Test 1.2: Sort by price descending
    result = get_products(products, sort_by="price", sort_order="desc")
    if result and result[0]["price"] >= result[-1]["price"]:
        print(f"✓ Sort by price desc: First=${result[0]['price']}, Last=${result[-1]['price']}")
    else:
        print("✗ Sort by price desc: Not properly sorted")

    # Test 1.3: Select specific fields
    result = get_products(products, fields=["id", "name"])
    if result and set(result[0].keys()) == {"id", "name"}:
        print(f"✓ Field selection: Only 'id' and 'name' fields returned")
    else:
        print(f"✗ Field selection: Expected {{'id', 'name'}}, got {set(result[0].keys()) if result else 'None'}")

    # Test 1.4: Combined operations
    result = get_products(
        products,
        filter_by={"in_stock": True},
        sort_by="price",
        sort_order="asc",
        fields=["id", "name", "price"]
    )
    if result and len(result) == 5 and result[0]["price"] <= result[-1]["price"]:
        print(f"✓ Combined: {len(result)} in-stock products, sorted by price asc")
    else:
        print("✗ Combined operations failed")

    print()
    print("=" * 60)
    print("TASK 2: fetch_with_retry() tests")
    print("=" * 60)

    # Test 2.1: Successful fetch (may take a few retries)
    try:
        result = fetch_with_retry("Implementation/products.json", max_retries=5)
        if result and "products" in result:
            print("✓ Fetch with retry: Successfully fetched data")
        else:
            print("✗ Fetch with retry: Invalid data returned")
    except Exception as e:
        print(f"✗ Fetch with retry: Raised {type(e).__name__}: {e}")

    # Test 2.2: Exhausted retries (use impossible file)
    try:
        # This should eventually fail after retries
        random.seed(0)  # Make it deterministic for testing
        result = fetch_with_retry("nonexistent.json", max_retries=2)
        print("✗ Exhausted retries: Should have raised an exception")
    except (ConnectionError, FileNotFoundError):
        print("✓ Exhausted retries: Properly raised exception after max retries")
    except Exception as e:
        print(f"? Exhausted retries: Raised {type(e).__name__} (acceptable)")

    print()
    print("=" * 60)
    print("TASK 3: get_all_similar_products() tests")
    print("=" * 60)

    # Test 3.1: Direct similar products
    result = get_all_similar_products("p005", products_map)
    if result == {"p003"}:
        print(f"✓ Direct similar: p005 -> {result}")
    else:
        print(f"✗ Direct similar: Expected {{'p003'}}, got {result}")

    # Test 3.2: Recursive traversal
    result = get_all_similar_products("p005", products_map)
    # p005 -> p003 -> p001, p005 -> ...
    # Full traversal from p005 should find multiple products
    result_full = get_all_similar_products("p005", products_map, max_depth=None)
    if result_full and len(result_full) > 1:
        print(f"✓ Recursive traversal: p005 connects to {len(result_full)} products: {result_full}")
    else:
        print(f"✗ Recursive traversal: Expected multiple products, got {result_full}")

    # Test 3.3: Cycle handling
    # p001 <-> p002 form a cycle
    result = get_all_similar_products("p001", products_map)
    if "p001" not in result and len(result) > 0:
        print(f"✓ Cycle handling: Didn't include starting product, found {result}")
    else:
        print(f"✗ Cycle handling: Issues with result {result}")

    # Test 3.4: Max depth limit
    result_depth1 = get_all_similar_products("p001", products_map, max_depth=1)
    result_depth2 = get_all_similar_products("p001", products_map, max_depth=2)
    if len(result_depth1) <= len(result_depth2):
        print(f"✓ Max depth: depth=1 -> {len(result_depth1)} products, depth=2 -> {len(result_depth2)} products")
    else:
        print(f"✗ Max depth: depth=1 should have <= products than depth=2")

    print()
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
