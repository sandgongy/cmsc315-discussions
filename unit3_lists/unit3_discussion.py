"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Inserting shifts later references right; front/middle edits are O(n).
    # End insertion is amortized O(1), though resizing can take O(n).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Reject negative indexes so a missing search result (-1) cannot
    # accidentally remove the last item. Check before mutating the list.
    if type(index) is not int or not 0 <= index < len(lst):
        return None
    # Later references shift left; removing the final item avoids that shift.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # No lookup table is available: inspect each value in order, O(n) worst case.
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    # Keep the original TODO prompt above; demonstrate each insertion below.
    tickets = ["Printer", "VPN", "Email"]
    print("Original tickets:", tickets)
    insert_at(tickets, 0, "Network outage")
    print("Beginning:", tickets)
    insert_at(tickets, len(tickets) // 2, "Account locked")
    print("Middle:", tickets)
    insert_at(tickets, len(tickets), "Software install")
    print("End:", tickets)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Display both the removed ticket and the remaining work.
    for label, index in [("Beginning", 0), ("Middle", len(tickets) // 2)]:
        removed = delete_at(tickets, index)
        print(f"{label}: removed {removed}; remaining: {tickets}")
    removed = delete_at(tickets, len(tickets) - 1)
    print(f"End: removed {removed}; remaining: {tickets}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # Use fresh data so earlier deletions cannot change the search setup.
    search_tickets = ["Printer", "VPN", "Email"]
    for value in ["VPN", "Missing ticket"]:
        print(f"Search {value!r}: index {search_value(search_tickets, value)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    # Empty input, invalid indexes, duplicates, and one-item boundaries.
    empty = []
    print("Delete from empty:", delete_at(empty, 0))
    print("Search empty:", search_value(empty, "VPN"))
    insert_at(empty, 0, "VPN")
    print("Insert into empty:", empty)
    print("Negative index rejected:", delete_at(empty, -1), empty)
    print("Index equal to length rejected:", delete_at(empty, len(empty)), empty)
    print("Noninteger index rejected:", delete_at(empty, "0"), empty)
    print("Delete only item:", delete_at(empty, 0), empty)
    print("Duplicate search returns first match:", search_value(["VPN", "VPN"], "VPN"))

    # A service-desk list keeps pending tickets in their planned order.
    print("\n=== SERVICE DESK SCENARIO ===")
    pending = ["Printer", "VPN", "Email"]
    insert_at(pending, 0, "Network outage")
    print("Urgent ticket added:", pending)
    index = search_value(pending, "VPN")
    if index != -1:
        print("Resolved ticket:", delete_at(pending, index))
    print("Remaining tickets:", pending)



if __name__ == "__main__":
    main()
