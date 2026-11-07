"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Each comparison chooses one subtree and skips the other.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)
        # Smaller IDs belong on the left; larger IDs belong on the right.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Equal IDs are ignored because employee IDs should be unique.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A comparison discards the entire subtree on the opposite side.
        # Balanced trees take O(log n); a chain can still take O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        # Left values are smaller and right values are larger, so this is sorted.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    employee_ids = [
        1050, 1025, 1075, 1010, 1030, 1060, 1090,
        1005, 1015, 1028, 1035, 1055, 1065, 1085, 1095,
    ]
    # This order gives both sides of the root several IDs.
    for employee_id in employee_ids:
        tree.insert(employee_id)
    print(f"Employee IDs inserted ({len(employee_ids)} total):", employee_ids)
    print("Smaller IDs went left; larger IDs went right at each node.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("Employee IDs in ascending order:", tree.inorder())
    print("Visiting left, node, then right lists smaller IDs first.")
    assert tree.inorder() == sorted(employee_ids)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Two existing IDs and two absent IDs exercise both search outcomes.
    for employee_id in [1025, 1095, 1000, 1080]:
        found = tree.search(employee_id)
        print(f"Employee ID {employee_id}: {'found' if found else 'not found'}")
        assert found == (employee_id in employee_ids)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    empty = BST()
    print("Empty tree traversal:", empty.inorder())
    print("Search empty tree for 1050:", empty.search(1050))
    assert empty.inorder() == [] and empty.search(1050) is False
    print("An empty root stops recursion: no values to visit or find.")

    tree.insert(1050)
    print("After inserting duplicate 1050:", tree.inorder())
    print(f"Duplicate IDs were ignored; the tree still contains {len(employee_ids)} IDs.")
    assert tree.inorder() == sorted(employee_ids)

    single = BST()
    single.insert(1040)
    print("Single ID:", single.inorder(), "| Found:", single.search(1040))
    assert single.inorder() == [1040] and single.search(1040)
    assert single.search(1041) is False
    print("Single-node search for missing 1041:", single.search(1041))

    # Same IDs, different insertion order: sorted inserts form a right chain.
    sequential = BST()
    for employee_id in sorted(employee_ids):
        sequential.insert(employee_id)
    print("Sorted-insertion traversal:", sequential.inorder())
    assert sequential.inorder() == sorted(employee_ids)
    # Count comparisons along the path to the largest ID in each tree.
    for label, example in [("Original insertion", tree), ("Sorted insertion", sequential)]:
        current = example.root
        comparisons = 0
        while current is not None:
            comparisons += 1
            if current.value == 1095:
                break
            current = current.left if 1095 < current.value else current.right
        print(f"{label}: finding 1095 took {comparisons} comparisons.")
        assert comparisons == (4 if example is tree else 15)
    print("Sorted insertion created a right-only chain; the same IDs took more work to search.")
    print("All checks passed.")



if __name__ == "__main__":
    main()
