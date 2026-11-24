"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    # The dictionary hashes each asset tag to locate its checkout record.
    checkouts = {}
    checkouts["LT-104"] = "Training"
    checkouts["LT-107"] = "Help Desk"
    checkouts["LT-112"] = "Operations"
    checkouts["LT-118"] = "Training"
    checkouts["LT-123"] = "Logistics"
    print("Active laptop checkouts:", checkouts)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # A lookup hashes the tag again and checks for a matching key.
    for tag in ("LT-104", "LT-107"):
        print(f"{tag} is checked out to {checkouts[tag]}.")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before reassignment:", checkouts)
    # Assigning an existing tag replaces its value and keeps the same entry count.
    checkouts["LT-104"] = "Operations"
    print("After reassignment:", checkouts)
    print(f"Active checkouts after reassignment: {len(checkouts)}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before return:", checkouts)
    # A returned laptop no longer has an active checkout record.
    del checkouts["LT-123"]
    print("After return:", checkouts)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    missing_tag = "LT-999"
    print(f"Lookup {missing_tag}: {checkouts.get(missing_tag, 'No active checkout')}")
    if checkouts.pop(missing_tag, None) is None:
        print(f"Delete {missing_tag}: No record to remove.")

    # Require a current checkout before allowing a reassignment.
    if missing_tag not in checkouts:
        print(f"Update {missing_tag}: No record to reassign.")

    empty_checkouts = {}
    print(f"Empty table lookup: {empty_checkouts.get('LT-104', 'No active checkout')}")

    # Reject a second checkout for the same asset without overwriting its record.
    duplicate_tag = "LT-104"
    if duplicate_tag in checkouts:
        print(f"Duplicate checkout {duplicate_tag}: Already assigned to {checkouts[duplicate_tag]}.")



if __name__ == "__main__":
    main()
