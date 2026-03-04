"""
List Comprehension + Dictionary Practice
Sierra Interview Prep

Instructions:
1. Read each problem and implement your solution
2. Run the file to check your answers: python Implementation/sierra/practice_list_comprehension.py
3. Solutions are at the bottom - don't peek until you've tried!

Difficulty: Similar to Sierra interview (filter/sort/fields)
"""

# ============================================================
# TEST DATA
# ============================================================

products = [
    {"id": "p001", "name": "Wireless Mouse", "price": 29.99, "category": "electronics", "in_stock": True, "rating": 4.5},
    {"id": "p002", "name": "Mechanical Keyboard", "price": 89.99, "category": "electronics", "in_stock": True, "rating": 4.8},
    {"id": "p003", "name": "USB Hub", "price": 24.99, "category": "accessories", "in_stock": False, "rating": 4.2},
    {"id": "p004", "name": "Monitor Stand", "price": 49.99, "category": "accessories", "in_stock": True, "rating": 4.0},
    {"id": "p005", "name": "Webcam", "price": 79.99, "category": "electronics", "in_stock": True, "rating": 4.6},
    {"id": "p006", "name": "Desk Lamp", "price": 34.99, "category": "home_office", "in_stock": True, "rating": 4.3},
    {"id": "p007", "name": "Cable Kit", "price": 19.99, "category": "accessories", "in_stock": False, "rating": 3.9},
]

users = [
    {"id": 1, "name": "Alice", "age": 28, "role": "admin", "active": True},
    {"id": 2, "name": "Bob", "age": 34, "role": "user", "active": True},
    {"id": 3, "name": "Charlie", "age": 22, "role": "user", "active": False},
    {"id": 4, "name": "Diana", "age": 45, "role": "admin", "active": True},
    {"id": 5, "name": "Eve", "age": 31, "role": "moderator", "active": False},
]

orders = [
    {"order_id": "o1", "user_id": 1, "items": ["p001", "p002"], "total": 119.98, "status": "shipped"},
    {"order_id": "o2", "user_id": 2, "items": ["p003"], "total": 24.99, "status": "pending"},
    {"order_id": "o3", "user_id": 1, "items": ["p005", "p006"], "total": 114.98, "status": "delivered"},
    {"order_id": "o4", "user_id": 3, "items": ["p001"], "total": 29.99, "status": "cancelled"},
    {"order_id": "o5", "user_id": 4, "items": ["p002", "p004", "p007"], "total": 159.97, "status": "shipped"},
]


# ============================================================
# LEVEL 1: Basic List Comprehension with Filter
# ============================================================

def problem_1():
    """
    Return all products that are in stock.
    Expected: 5 products (p001, p002, p004, p005, p006)
    """

    result = [p for p in products if p["in_stock"] == True]
    return result


def problem_2():
    """
    Return all products in the "electronics" category.
    Expected: 3 products
    """
    result = [p for p in products if p["category"] == "electronics"]
    return result


def problem_3():
    """
    Return all products with price > 30.
    Expected: 4 products (p002, p004, p005, p006)
    """
    # YOUR CODE HERE
    result = [p for p in products if p["price"] > 30]
    return result


def problem_4():
    """
    Return all active users.
    Expected: 3 users (Alice, Bob, Diana)
    """
    result = [u for u in users if u["active"]]
    return result


# ============================================================
# LEVEL 2: Dict Comprehension (Field Selection)
# ============================================================

def problem_5():
    """
    From products, return only "id" and "name" fields.
    Expected: [{"id": "p001", "name": "Wireless Mouse"}, ...]
    """
    fields = ["id", "name"]
    result = [{key: products[key] for key in fields if key in products} for ]
    return result


def problem_6():
    """
    From users, return only "name" and "role" fields.
    Expected: [{"name": "Alice", "role": "admin"}, ...]
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_7():
    """
    Given a list of field names, select only those fields from products.
    fields = ["id", "name", "price"]
    """
    fields = ["id", "name", "price"]
    # YOUR CODE HERE
    result = None
    return result


# ============================================================
# LEVEL 3: Multiple Conditions (AND / OR)
# ============================================================

def problem_8():
    """
    Return products that are BOTH in stock AND in electronics category.
    Expected: 3 products (p001, p002, p005)
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_9():
    """
    Return products that are EITHER out of stock OR priced under $25.
    Expected: 3 products (p003, p007, p007) - wait, that's wrong
    Actually: p003 (out of stock), p007 (both), and p007's price is 19.99
    So: p003, p007 (out of stock) + any under $25 = p003, p007
    Actually p003=$24.99, p007=$19.99 are both out of stock AND under/at $25
    Expected: p003, p007
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_10():
    """
    Return users who are admins AND active.
    Expected: 2 users (Alice, Diana)
    """
    # YOUR CODE HERE
    result = None
    return result


# ============================================================
# LEVEL 4: Using all() and any()
# ============================================================

def problem_11():
    """
    Given filter criteria as a dict, return products matching ALL criteria.
    criteria = {"in_stock": True, "category": "electronics"}
    Expected: 3 products (p001, p002, p005)
    """
    criteria = {"in_stock": True, "category": "electronics"}
    # YOUR CODE HERE (use all())
    result = None
    return result


def problem_12():
    """
    Given filter criteria as a dict, return products matching ANY criteria.
    criteria = {"category": "home_office", "price": 29.99}
    Expected: p001 (price matches), p006 (category matches)
    """
    criteria = {"category": "home_office", "price": 29.99}
    # YOUR CODE HERE (use any())
    result = None
    return result


def problem_13():
    """
    Return products where ALL of these are true:
    - in_stock is True
    - price < 50
    - rating >= 4.0
    Use all() with a list of conditions.
    Expected: p001, p004, p006
    """
    # YOUR CODE HERE
    result = None
    return result


# ============================================================
# LEVEL 5: Combined Filter + Transform
# ============================================================

def problem_14():
    """
    Return ONLY the names of products that are in stock.
    Expected: ["Wireless Mouse", "Mechanical Keyboard", "Monitor Stand", "Webcam", "Desk Lamp"]
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_15():
    """
    Return products in stock with only id, name, price fields.
    Expected: [{"id": "p001", "name": "Wireless Mouse", "price": 29.99}, ...]
    """
    fields = ["id", "name", "price"]
    # YOUR CODE HERE
    result = None
    return result


def problem_16():
    """
    Return electronics products, sorted by price ascending, with only name and price.
    Expected: [{"name": "Wireless Mouse", "price": 29.99}, {"name": "Webcam", "price": 79.99}, {"name": "Mechanical Keyboard", "price": 89.99}]
    """
    # YOUR CODE HERE (filter -> sort -> select)
    result = None
    return result


# ============================================================
# LEVEL 6: Dictionary Transformations
# ============================================================

def problem_17():
    """
    Create a dict mapping product id -> name.
    Expected: {"p001": "Wireless Mouse", "p002": "Mechanical Keyboard", ...}
    """
    # YOUR CODE HERE (dict comprehension)
    result = None
    return result


def problem_18():
    """
    Create a dict mapping product id -> price, but only for in-stock items.
    Expected: {"p001": 29.99, "p002": 89.99, "p004": 49.99, "p005": 79.99, "p006": 34.99}
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_19():
    """
    Create a dict mapping user id -> user name.
    Expected: {1: "Alice", 2: "Bob", 3: "Charlie", 4: "Diana", 5: "Eve"}
    """
    # YOUR CODE HERE
    result = None
    return result


# ============================================================
# LEVEL 7: Nested / Complex
# ============================================================

def problem_20():
    """
    Return all unique product IDs from all orders.
    (Flatten the items lists from all orders into a single set)
    Expected: {"p001", "p002", "p003", "p004", "p005", "p006", "p007"}
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_21():
    """
    For each order, return a dict with order_id and item_count (number of items).
    Expected: [{"order_id": "o1", "item_count": 2}, {"order_id": "o2", "item_count": 1}, ...]
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_22():
    """
    Return orders that have more than 1 item AND total > 100.
    Expected: 2 orders (o1, o5)
    """
    # YOUR CODE HERE
    result = None
    return result


def problem_23():
    """
    Given a dynamic list of fields, select those fields from products.
    If a field doesn't exist in a product, skip it (don't error).
    fields = ["id", "name", "nonexistent_field"]
    Expected: [{"id": "p001", "name": "Wireless Mouse"}, ...]
    """
    fields = ["id", "name", "nonexistent_field"]
    # YOUR CODE HERE
    result = None
    return result


# ============================================================
# LEVEL 8: Sierra Interview Style
# ============================================================

def problem_24():
    """
    Implement the full get_products function.
    - Filter by filter_by dict (all must match)
    - Sort by sort_by field
    - Select only fields in fields list

    Test: filter_by={"in_stock": True, "category": "electronics"}
          sort_by="price"
          sort_order="desc"
          fields=["id", "name", "price"]
    Expected: electronics in stock, sorted by price desc, with 3 fields
    """
    filter_by = {"in_stock": True, "category": "electronics"}
    sort_by = "price"
    sort_order = "desc"
    fields = ["id", "name", "price"]

    # YOUR CODE HERE
    result = None
    return result


def problem_25():
    """
    CHALLENGE: Write a one-liner that does all of problem 24.
    (Hint: chain sorted() with list comprehension)
    """
    filter_by = {"in_stock": True, "category": "electronics"}
    sort_by = "price"
    fields = ["id", "name", "price"]

    # YOUR CODE HERE (one line!)
    result = None
    return result


# ============================================================
# RUNNER
# ============================================================

def run_tests():
    print("=" * 60)
    print("LIST COMPREHENSION PRACTICE")
    print("=" * 60)
    print()

    tests = [
        (problem_1, "L1: In-stock products", lambda r: r and len(r) == 5),
        (problem_2, "L1: Electronics category", lambda r: r and len(r) == 3),
        (problem_3, "L1: Price > 30", lambda r: r and len(r) == 4),
        (problem_4, "L1: Active users", lambda r: r and len(r) == 3),
        (problem_5, "L2: Select id, name", lambda r: r and set(r[0].keys()) == {"id", "name"}),
        (problem_6, "L2: Select name, role", lambda r: r and set(r[0].keys()) == {"name", "role"}),
        (problem_7, "L2: Dynamic fields", lambda r: r and set(r[0].keys()) == {"id", "name", "price"}),
        (problem_8, "L3: In stock AND electronics", lambda r: r and len(r) == 3),
        (problem_9, "L3: Out of stock OR under $25", lambda r: r and len(r) == 2),
        (problem_10, "L3: Admin AND active", lambda r: r and len(r) == 2),
        (problem_11, "L4: all() with criteria", lambda r: r and len(r) == 3),
        (problem_12, "L4: any() with criteria", lambda r: r and len(r) == 2),
        (problem_13, "L4: all() multiple conditions", lambda r: r and len(r) == 3),
        (problem_14, "L5: Names of in-stock", lambda r: r and len(r) == 5 and isinstance(r[0], str)),
        (problem_15, "L5: In-stock with fields", lambda r: r and len(r) == 5 and set(r[0].keys()) == {"id", "name", "price"}),
        (problem_16, "L5: Filter + sort + select", lambda r: r and len(r) == 3 and r[0]["price"] == 29.99),
        (problem_17, "L6: id -> name dict", lambda r: r and r.get("p001") == "Wireless Mouse"),
        (problem_18, "L6: id -> price (in-stock)", lambda r: r and len(r) == 5 and "p003" not in r),
        (problem_19, "L6: user id -> name", lambda r: r and r.get(1) == "Alice"),
        (problem_20, "L7: Unique product IDs from orders", lambda r: r and len(r) == 7),
        (problem_21, "L7: Order item counts", lambda r: r and r[0].get("item_count") == 2),
        (problem_22, "L7: Orders with >1 item AND >100 total", lambda r: r and len(r) == 2),
        (problem_23, "L7: Dynamic fields (skip missing)", lambda r: r and "nonexistent_field" not in r[0]),
        (problem_24, "L8: Full get_products", lambda r: r and len(r) == 3 and r[0]["price"] == 89.99),
        (problem_25, "L8: One-liner challenge", lambda r: r and len(r) == 3),
    ]

    passed = 0
    for func, name, check in tests:
        try:
            result = func()
            if result is None:
                print(f"[ ] {name} - Not implemented")
            elif check(result):
                print(f"[X] {name} - PASSED")
                passed += 1
            else:
                print(f"[-] {name} - Wrong answer: {result[:2] if isinstance(result, list) else result}...")
        except Exception as e:
            print(f"[!] {name} - Error: {e}")

    print()
    print(f"Score: {passed}/{len(tests)}")
    print()


# ============================================================
# SOLUTIONS (scroll down when ready)
# ============================================================
"""























SOLUTIONS BELOW - TRY THE PROBLEMS FIRST!























"""

SOLUTIONS = '''
# Problem 1
result = [p for p in products if p["in_stock"]]

# Problem 2
result = [p for p in products if p["category"] == "electronics"]

# Problem 3
result = [p for p in products if p["price"] > 30]

# Problem 4
result = [u for u in users if u["active"]]

# Problem 5
result = [{"id": p["id"], "name": p["name"]} for p in products]

# Problem 6
result = [{"name": u["name"], "role": u["role"]} for u in users]

# Problem 7
result = [{k: p[k] for k in fields} for p in products]

# Problem 8
result = [p for p in products if p["in_stock"] and p["category"] == "electronics"]

# Problem 9
result = [p for p in products if not p["in_stock"] or p["price"] < 25]

# Problem 10
result = [u for u in users if u["role"] == "admin" and u["active"]]

# Problem 11
result = [p for p in products if all(p.get(k) == v for k, v in criteria.items())]

# Problem 12
result = [p for p in products if any(p.get(k) == v for k, v in criteria.items())]

# Problem 13
result = [p for p in products if all([p["in_stock"], p["price"] < 50, p["rating"] >= 4.0])]

# Problem 14
result = [p["name"] for p in products if p["in_stock"]]

# Problem 15
result = [{k: p[k] for k in fields} for p in products if p["in_stock"]]

# Problem 16
filtered = [p for p in products if p["category"] == "electronics"]
sorted_products = sorted(filtered, key=lambda x: x["price"])
result = [{"name": p["name"], "price": p["price"]} for p in sorted_products]

# Problem 17
result = {p["id"]: p["name"] for p in products}

# Problem 18
result = {p["id"]: p["price"] for p in products if p["in_stock"]}

# Problem 19
result = {u["id"]: u["name"] for u in users}

# Problem 20
result = {item for order in orders for item in order["items"]}

# Problem 21
result = [{"order_id": o["order_id"], "item_count": len(o["items"])} for o in orders]

# Problem 22
result = [o for o in orders if len(o["items"]) > 1 and o["total"] > 100]

# Problem 23
result = [{k: p[k] for k in fields if k in p} for p in products]

# Problem 24
filtered = [p for p in products if all(p.get(k) == v for k, v in filter_by.items())]
sorted_products = sorted(filtered, key=lambda x: x[sort_by], reverse=(sort_order == "desc"))
result = [{k: p[k] for k in fields} for p in sorted_products]

# Problem 25 (one-liner)
result = [{k: p[k] for k in fields} for p in sorted([p for p in products if all(p.get(k) == v for k, v in filter_by.items())], key=lambda x: x[sort_by], reverse=True)]
'''


if __name__ == "__main__":
    run_tests()
    print("\nSolutions are at the bottom of the file.")
    print("Run: python Implementation/sierra/practice_list_comprehension.py")
