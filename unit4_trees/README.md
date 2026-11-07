# Unit 4: Binary Search Trees

I used employee ID numbers to show how a BST organized values and narrowed down searches. I completed the starter's recursive insertion, search, and in-order traversal methods and kept the original TODO prompts and comments.

## What I changed

Each node stored an ID and references to its left and right children. Insertion placed smaller IDs on the left and larger IDs on the right. Each recursive call returned its node so the parent kept the connection to its child. I ignored duplicates because the example treated employee IDs as unique.

Search followed the same comparisons and returned False when it reached an empty position. In-order traversal visited the left subtree, the current ID, and the right subtree, which produced ascending output.

## Running the program

From this folder, I ran:

```bash
python3 unit4_discussion.py
```

The program used Python 3 and no extra packages. I checked the results with assertions as well as printed output.

## Results

| Check | Result |
| --- | --- |
| Inserted seven IDs | 1050, 1025, 1075, 1010, 1030, 1060, 1090 |
| In-order traversal | [1010, 1025, 1030, 1050, 1060, 1075, 1090] |
| Existing IDs 1025 and 1090 | Both returned True |
| Missing IDs 1000 and 1080 | Both returned False |
| Empty tree | Traversal returned []; search returned False |
| Duplicate 1050 | Traversal still contained seven unique IDs |
| Single-node tree | 1040 was found; 1041 was not found |
| Original insertion order | Finding 1090 took three comparisons |
| Sorted insertion order | Finding 1090 took seven comparisons |

All assertions passed. The two insertion orders produced identical sorted output, but different search paths. This showed why sorted output alone did not prove that a tree was balanced.

## Performance and limits

The original order produced a balanced tree for these seven IDs. A balanced BST supported search and insertion in O(log n) time; a skewed tree required O(n) in the worst case. Traversal visited every node and took O(n) either way. An unsorted list could require a linear search, while a sorted array could also support O(log n) binary search. The BST's ordering helped it skip an entire subtree at each comparison, although it did not always skip half the values.

I used fixed integer IDs for this demonstration. I did not add interactive input or validation for mixed types. The tree did not rebalance itself, and a very long chain could exceed Python's recursion limit. A self-balancing tree would address the height problem for a larger application. The example stored IDs only; a full employee directory would also need employee details associated with each ID.

## Reflection

This assignment showed me how recursion connected the smaller parts of a tree. Insertion and search followed the same comparison rule, while traversal visited both sides to collect every value. Returning the updated node reference was the part that needed the most attention because the parent still needed a connection to the new child. The employee ID example made that relationship easier to follow.

The comparison test also showed why using a BST did not automatically make searching fast. Both trees contained the same IDs and printed the same sorted list, but finding 1090 took three comparisons in the first tree and seven after sorted insertion. A balanced tree could keep searches near O(log n), while a chain could behave like a linked list and require O(n). An unsorted list also required up to O(n) for a search, although a sorted array could use binary search. The main lesson was that insertion order affected the tree's shape, and that shape affected how much work each search needed.
