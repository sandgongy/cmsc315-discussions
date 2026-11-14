"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # In the worst case, every item is checked once: O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        # Sorted order lets us discard half; moving past mid avoids loops.
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def show_result(values, target, expected):
    """Check expected indexes and display both results clearly."""
    linear = linear_search(values, target)
    binary = binary_search(values, target)
    assert linear == expected, (target, linear, expected)
    assert binary == expected, (target, binary, expected)
    print(f"Target {target}: linear={linear}, binary={binary}; PASS")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small = [101, 105, 112, 118, 124, 130]
    print("Sorted IT equipment IDs:", small)
    for target, expected in [(118, 3), (119, -1)]:
        show_result(small, target, expected)
    # 118 is at index 3; 119 is absent, so both searches return -1.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large = list(range(100000))
    for target, expected in [(99999, 99999), (100000, -1)]:
        show_result(large, target, expected)
    # A full scan may check 100,000 items; binary search needs at most 17
    # middle checks. Dataset creation and sorting are outside these timings.
    from timeit import timeit
    for search in (linear_search, binary_search):
        elapsed = timeit(lambda: search(large, 99999), number=100) / 100
        print(f"{search.__name__}: {elapsed * 1000:.6f} ms/search (100 runs)")
    print("Worst case: linear O(n); binary O(log n). Timings vary by run.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    cases = [
        ("empty list", [], 5, -1),
        ("single item found", [5], 5, 0),
        ("single item missing", [5], 6, -1),
        ("first position", small, 101, 0),
        ("last position", small, 130, 5),
        ("below range", small, 100, -1),
        ("above range", small, 131, -1),
        ("duplicate IDs", [1, 2, 2, 3], 2, 1),
    ]
    for label, values, target, expected in cases:
        print(label)
        show_result(values, target, expected)
    print("All 8 edge cases passed. Missing targets safely returned -1.")

    print("\n=== EQUIPMENT DELIVERY EXAMPLE ===")
    delivery = [118, 101, 130, 105, 124, 112]
    inventory = sorted(delivery)
    print("Unsorted delivery, linear index:", linear_search(delivery, 124))
    print("Sorted inventory, binary index:", binary_search(inventory, 124))
    # Indexes refer to their own lists; sorting changes item positions.
    print("Linear search avoided sorting for one delivery lookup.")
    print("A sorted inventory supported repeated binary searches.")


if __name__ == "__main__":
    main()
