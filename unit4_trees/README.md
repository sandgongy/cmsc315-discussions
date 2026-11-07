# Unit 4: Binary Search Trees

I decided to use employee ID numbers for a demonstration of how a BST works and can be used to search for values. I completed the starter code for recursive insertion, search and in-order traversal, leaving the original TODO comments and instructions as they were.

## What I changed

The node stores the ID of the employee and references to the left and right children. The IDs of the left children are smaller than the ID of the parent, and the IDs of the right children are larger than the ID of the parent. The recursive call returns the child that was just inserted, so the parent can keep a reference to its child. I ignored duplicates in this example because the IDs are treated as unique for the employees.

Search is similar to the insertion code, except that when a node with a NULL left or right child is reached, False is returned. In-order traversal visits the left subtree first, then the current node, then the right subtree. This produces a list of the IDs in ascending order.

## Running the program

From this folder, I ran:

```bash
python3 unit4_discussion.py
```

I used Python 3 and no extra packages for the exercise. The code is tested with assertions as well as printed output.

## Results

I have expanded the minimum requirement of seven employee IDs to fifteen employee IDs across four levels.

| Check | Result |
| --- | --- |
| Inserted fifteen IDs | 1050, 1025, 1075, 1010, 1030, 1060, 1090, 1005, 1015, 1028, 1035, 1055, 1065, 1085, 1095 |
| In-order traversal | [1005, 1010, 1015, 1025, 1028, 1030, 1035, 1050, 1055, 1060, 1065, 1075, 1085, 1090, 1095] |
| Existing IDs 1025 and 1095 | Both returned True |
| Missing IDs 1000 and 1080 | Both returned False |
| Empty tree | Traversal returned []; search returned False |
| Duplicate 1050 | Traversal still contained fifteen unique IDs |
| Single-node tree | 1040 was found; 1041 was not found |
| Original insertion order | Finding 1095 took four comparisons |
| Sorted insertion order | Finding 1095 took fifteen comparisons |

All assertions passed. The two insertion orders produced identical sorted output, but different search paths. This showed why sorted output alone did not prove that a tree was balanced.

## Performance and limits

The tree created with the original insertion order is a balanced tree for the fifteen IDs used in the demonstration. A balanced BST can be searched and inserted in O(log n) time. A skewed tree would take O(n) in the worst case for both operations. Traversal would still take O(n) in either case. For an unsorted list of items, the search would take O(n) in the worst case, but a sorted array of the same items could be searched in O(log n) time using binary search. The BST can skip over an entire subtree at each step in the search, but it does not necessarily have to skip over half of the items.

The example uses fixed integer IDs for employees. I did not add interactive input or any kind of validation for mixed types. The tree does not automatically rebalance itself. A very long chain of nodes could even exceed the maximum recursion depth allowed by Python. A self-balancing tree would be a better choice for a larger application. The example stores only the IDs for employees. A full employee directory would also store more information about each employee such as name, email, department, etc.

## Reflection

This assignment showed me how to use recursion to go through the smaller parts of a tree. The insertion and search methods used the same comparison as the in-order traversal to visit the left and right subtrees. The only change was to return the updated node reference in the insertion and search methods, instead of printing out the values as in the in-order traversal. The employee ID example made it easy to see how the parent-child relationship was being maintained.

This example also demonstrated that while a BST can make search fast, it does not automatically do so. Both trees above contained the same IDs and when printed in sorted order they were identical. However, in the first tree above, finding 1095 took four comparisons while in the second tree, finding 1095 took fifteen comparisons. The balanced tree above kept searches near O(log n) while the chain above was like a linked list and took O(n) to find 1095. An unsorted list of items would take up to O(n) to find an item but a sorted array could take O(log n) time to find an item using binary search. It is the shape of the tree that is determined by the order in which items are inserted that determines the number of comparisons that are required to find an item.
