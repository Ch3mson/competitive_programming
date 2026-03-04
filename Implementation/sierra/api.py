"""
Sierra Interview - API Module (DO NOT MODIFY)

This module simulates a Shopify-like Products API with artificial network latency.
Read through this file to understand the API behavior, but do not modify it.

The API has intentional jitter that causes timeouts. Your task is to work around
this in sierra.py by implementing proper retry logic.

Key constants to note:
- MIN_RESPONSE_TIME: Minimum time the API takes to respond
- MAX_RESPONSE_TIME: Maximum time the API takes to respond
- TIMEOUT: Time after which a request is considered failed

Hint: Notice the relationship between these constants...
"""

import json
import time
import random
import os
from typing import Dict, List, Optional

_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# CONFIGURATION CONSTANTS (Read these carefully!)
# ============================================================

MIN_RESPONSE_TIME = 2.0  # Minimum API response time in seconds
MAX_RESPONSE_TIME = 5.0  # Maximum API response time in seconds
TIMEOUT = 3.0            # Request timeout in seconds

# Internal state
_products_data: Optional[List[Dict]] = None


def _load_products() -> List[Dict]:
    """Load products from JSON file (internal use only)."""
    global _products_data
    if _products_data is None:
        with open(os.path.join(_DIR, "sierra_products.json"), "r") as f:
            data = json.load(f)
            _products_data = data["products"]
    return _products_data


class APITimeoutError(Exception):
    """Raised when API request times out."""
    pass


class APIError(Exception):
    """Raised for general API errors."""
    pass


def fetch_products() -> List[Dict]:
    """
    Fetch all products from the API.

    This function simulates network latency with random jitter.
    Response time varies between MIN_RESPONSE_TIME and MAX_RESPONSE_TIME.

    Returns:
        List of product dictionaries

    Raises:
        APITimeoutError: If the request takes longer than TIMEOUT
        APIError: For other API failures (rare)
    """
    # Simulate network latency with jitter
    response_time = random.uniform(MIN_RESPONSE_TIME, MAX_RESPONSE_TIME)

    # Simulate the wait
    time.sleep(min(response_time, TIMEOUT + 0.1))

    # Check if we timed out
    if response_time > TIMEOUT:
        raise APITimeoutError(
            f"Request timed out after {TIMEOUT}s (would have taken {response_time:.2f}s)"
        )

    # Small chance of random failure
    if random.random() < 0.05:
        raise APIError("Internal server error")

    # Success - return the products
    return _load_products()


def get_product_by_id(product_id: str) -> Optional[Dict]:
    """
    Fetch a single product by ID.

    This is a faster endpoint with less jitter, but still has some latency.

    Args:
        product_id: The product ID to look up

    Returns:
        Product dictionary if found, None otherwise

    Raises:
        APITimeoutError: If the request takes too long
    """
    # Less jitter for single product lookup
    response_time = random.uniform(0.5, 1.5)
    time.sleep(response_time)

    if response_time > 1.2:
        raise APITimeoutError("Single product lookup timed out")

    products = _load_products()
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# ============================================================
# DO NOT MODIFY ANYTHING ABOVE THIS LINE
# ============================================================

if __name__ == "__main__":
    # Quick test - run this a few times to see the timeout behavior
    print("Testing API fetch_products()...")
    print(f"MIN_RESPONSE_TIME: {MIN_RESPONSE_TIME}s")
    print(f"MAX_RESPONSE_TIME: {MAX_RESPONSE_TIME}s")
    print(f"TIMEOUT: {TIMEOUT}s")
    print()

    for i in range(3):
        print(f"Attempt {i + 1}...")
        try:
            start = time.time()
            products = fetch_products()
            elapsed = time.time() - start
            print(f"  Success! Got {len(products)} products in {elapsed:.2f}s")
        except APITimeoutError as e:
            print(f"  Timeout: {e}")
        except APIError as e:
            print(f"  Error: {e}")
        print()
