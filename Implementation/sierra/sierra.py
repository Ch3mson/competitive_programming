"""
Sierra Interview Challenge - Products API

You are working with a products catalog API. The API (in api.py) is flaky and
has artificial latency. Your task is to implement three functions to work with
this API reliably.

Instructions:
1. Read through api.py to understand the API behavior and constants
2. Implement the three functions below
3. Run this file to test your implementation: python Implementation/sierra/sierra.py

Time estimate: ~45-60 minutes

Good luck!
"""

from typing import List, Dict, Any, Optional, Set


# ============================================================
# PART 1: Get Products (Filter, Sort, Select Fields)
# ============================================================

def get_products(
    products: List[Dict],
    filter_by: Optional[Dict[str, Any]] = None,
    sort_by: Optional[str] = None,
    sort_order: str = "asc",
    fields: Optional[List[str]] = None
) -> List[Dict]:
    """
    Process a list of products with filtering, sorting, and field selection.

    Args:
        products: List of product dictionaries
        filter_by: Dict of field->value pairs to filter by
                   Example: {"category": "electronics", "in_stock": True}
        sort_by: Field name to sort by (e.g., "price", "name")
        sort_order: "asc" for ascending, "desc" for descending
        fields: List of fields to include in output
                Example: ["id", "name", "price"]
                If None, include all fields

    Returns:
        Processed list of products

    Example:
        >>> get_products(products,
        ...     filter_by={"in_stock": True},
        ...     sort_by="price",
        ...     sort_order="desc",
        ...     fields=["id", "name", "price"])
        [{"id": "p004", "name": "USB-C Docking Station", "price": 149.99}, ...]
    """
    # first filter_by specifications
    filtered_products = []
    if filter_by:
        filtered_products = [p for p in products if (all(p.get(key) == value for key, value in filter_by.items()))]
    else:
        filtered_products = products

    sorted_products = []
    if sort_by:
        sorted_products = sorted(filtered_products, key=lambda item: item[sort_by], reverse = False if sort_order == "asc" else True)
    else:
        sorted_products = filtered_products
    
    filtered_product_fields = []
    if fields:
        filtered_product_fields = [{key: p[key] for key in fields if key in p} for p in sorted_products]
    else:
        filtered_product_fields = sorted_products

    return filtered_product_fields
# ============================================================
# PART 2: Fetch Products with Retry Logic
# ============================================================

def fetch_products_with_retry(max_retries: int = 5) -> List[Dict]:
    """
    Fetch products from the API with retry logic for handling failures.

    The API (see api.py) has intentional latency and timeout issues.
    You need to implement retry logic that handles:
    - APITimeoutError: The request took too long
    - APIError: General API failures

    HINT: Look at the constants in api.py:
    - MIN_RESPONSE_TIME
    - MAX_RESPONSE_TIME
    - TIMEOUT

    Think about how these relate to each other and what strategy
    would give you the best chance of success.

    Args:
        max_retries: Maximum number of retry attempts

    Returns:
        List of product dictionaries

    Raises:
        Exception: If all retries are exhausted
    """
    # Import the API module
    from api import fetch_products, APITimeoutError, APIError

    products = []
    for i in range(max_retries):
        if not products:
            try:
                products = fetch_products()
            except APITimeoutError:
                print("API TIMEOUT ERROR")
            except APIError:
                print("API ERROR")
        else:
            break
    print(products)
    return products
    # TODO: Implement retry logic here
    # Consider: What's the relationship between MIN_RESPONSE_TIME and TIMEOUT?

    pass


# ============================================================
# PART 3: Get All Recommendations (DFS Traversal)
# ============================================================

def get_all_recommendations(
    product_id: str,
    products: List[Dict],
    max_depth: Optional[int] = None
) -> Set[str]:
    """
    Recursively find all recommended products using DFS traversal.

    Starting from a product, follow the "similar_products" links to find
    all reachable products. Products can reference each other (cycles exist),
    so you must handle this to avoid infinite loops.

    Args:
        product_id: Starting product ID
        products: List of all product dictionaries
        max_depth: Optional maximum recursion depth (None = unlimited)

    Returns:
        Set of all reachable product IDs (excluding the starting product)

    Example:
        If p001 -> [p002, p003] and p002 -> [p004, p001]
        get_all_recommendations("p001", products) returns {"p002", "p003", "p004"}
        (Note: p001 is NOT included even though p002 points back to it)

    Important:
        - Handle cycles! Products can reference each other.
        - A product should not appear in its own recommendations.
        - If max_depth is provided, limit how far you traverse.
    """
    id_similar_products = {}
    for p in products:
        id_similar_products[p["id"]] = p["similar_products"]
    visited = set()
    output = []

    def dfs(p):
        if p not in id_similar_products:
            return
        for nei in id_similar_products[p]:
            if nei not in visited:
                visited.add(nei)
                output.append(nei)
                dfs(nei)

    visited.add(product_id)
    dfs(product_id)
    return set(output)

# ============================================================
# Helper Function (provided)
# ============================================================

def build_products_map(products: List[Dict]) -> Dict[str, Dict]:
    """Convert list of products to a dict keyed by product ID."""
    return {p["id"]: p for p in products}


# ============================================================
# MAIN - Test your implementation
# ============================================================

def main():
    print("=" * 60)
    print("SIERRA INTERVIEW CHALLENGE")
    print("=" * 60)
    print()

    # ---- PART 2: Fetch with Retry ----
    print("PART 2: Fetching products with retry logic...")
    print("-" * 40)

    try:
        products = fetch_products_with_retry(max_retries=5)
        if products:
            print(f"SUCCESS: Fetched {len(products)} products")
        else:
            print("FAILED: No products returned")
            return
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")
        print()
        print("Hint: Check api.py for the timing constants.")
        print("What's the relationship between MIN_RESPONSE_TIME and TIMEOUT?")
        return

    print()

    # ---- PART 1: Get Products ----
    print("PART 1: Testing get_products()...")
    print("-" * 40)

    # Test 1.1: Filter by category
    result = get_products(products, filter_by={"category": "electronics"})
    if result:
        print(f"Filter by category='electronics': {len(result)} products")
        for p in result[:3]:
            print(f"  - {p.get('name', p)}")
    else:
        print("Filter by category: Not implemented or returned None")

    # Test 1.2: Sort by price
    result = get_products(products, sort_by="price", sort_order="desc")
    if result:
        print(f"Sort by price (desc): First={result[0].get('name')}, Last={result[-1].get('name')}")
    else:
        print("Sort by price: Not implemented or returned None")

    # Test 1.3: Select fields
    result = get_products(products, fields=["id", "name", "price"])
    if result:
        print(f"Select fields [id, name, price]: Keys = {set(result[0].keys())}")
    else:
        print("Select fields: Not implemented or returned None")

    # Test 1.4: Combined
    result = get_products(
        products,
        filter_by={"in_stock": True, "category": "electronics"},
        sort_by="price",
        sort_order="asc",
        fields=["id", "name", "price"]
    )
    if result:
        print(f"Combined (in-stock electronics, sorted by price asc, 3 fields):")
        for p in result[:3]:
            print(f"  - ${p.get('price', '?')}: {p.get('name', p)}")
    else:
        print("Combined operations: Not implemented or returned None")

    print()

    # ---- PART 3: DFS Recommendations ----
    print("PART 3: Testing get_all_recommendations()...")
    print("-" * 40)

    # Test 3.1: Basic traversal
    result = get_all_recommendations("p001", products)
    if result:
        print(f"Recommendations from p001: {len(result)} products")
        print(f"  IDs: {sorted(result)}")
    else:
        print("Basic traversal: Not implemented or returned None")

    # Test 3.2: Check cycle handling (p001 <-> p002 <-> p003 forms a cycle)
    result = get_all_recommendations("p002", products)
    if result and "p002" not in result:
        print(f"Cycle handling: OK - p002 not in its own recommendations")
    elif result:
        print(f"Cycle handling: WARNING - starting product in results")
    else:
        print("Cycle handling: Not implemented")

    # Test 3.3: Max depth
    result_d1 = get_all_recommendations("p001", products, max_depth=1)
    result_d2 = get_all_recommendations("p001", products, max_depth=2)
    result_all = get_all_recommendations("p001", products)
    if result_d1 and result_d2:
        print(f"Max depth test: depth=1 -> {len(result_d1)}, depth=2 -> {len(result_d2)}, unlimited -> {len(result_all) if result_all else '?'}")
    else:
        print("Max depth: Not implemented")

    # Test 3.4: Isolated product (p011 only points to p010)
    result = get_all_recommendations("p011", products)
    if result:
        print(f"From p011 (Cable Management Kit): {result}")
    else:
        print("Isolated product test: Not implemented")

    print()
    print("=" * 60)
    print("Challenge complete! Review your output above.")
    print("=" * 60)


if __name__ == "__main__":
    main()
