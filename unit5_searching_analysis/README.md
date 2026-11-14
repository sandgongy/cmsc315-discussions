# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Implementation

I implemented `linear_search` by iterating through the list and returning the first index that contains the item, or `-1` if the item is not in the list. I implemented `binary_search` by initializing `low`, `high`, and `mid` indexes. In the case where the mid value is not equal to the item being searched for, the boundary is moved past mid, thus eliminating half of the search space. I also preserved the TODOs in the starter code and added some comments to better explain the code that was implemented.

## Requirements and results

### 1. Test both algorithms on a small dataset

I used a list of six sorted IT equipment IDs: `[101, 105, 112, 118, 124, 130]`. For both algorithms, the search for the ID `118` resulted in the index `3` and the search for the missing ID `119` resulted in `-1`.

### 2. Test both algorithms on a large dataset

I tested both algorithms on a list of 100,000 integers sorted in ascending order from `0` through `99999`. In both cases, the last value in the list was found at index `99999`, and for value `100000`, both algorithms returned `-1`.

| Dataset | Target | Linear result | Binary result |
| --- | ---: | ---: | ---: |
| Six equipment IDs | 118 | 3 | 3 |
| Six equipment IDs | 119 | -1 | -1 |
| 100,000 integers | 99999 | 99999 | 99999 |
| 100,000 integers | 100000 | -1 | -1 |

All four dataset checks passed. The program checked the returned indexes with assertions before printing PASS.

### 3. Demonstrate edge cases

I tested the following eight cases. Both algorithms returned the expected result in each test.

| Edge case | Input | Target | Result from each search |
| --- | --- | ---: | ---: |
| Empty list | `[]` | 5 | -1 |
| Single item found | `[5]` | 5 | 0 |
| Single item missing | `[5]` | 6 | -1 |
| First position | Six equipment IDs | 101 | 0 |
| Last position | Six equipment IDs | 130 | 5 |
| Below the range | Six equipment IDs | 100 | -1 |
| Above the range | Six equipment IDs | 131 | -1 |
| Duplicate IDs | `[1, 2, 2, 3]` | 2 | 1 |

The empty list returned `-1` without accessing an item. The first and last position tests checked the search boundaries. Linear search returned the first matching duplicate. Binary search could return any matching duplicate; it returned index `1` for this particular test.

### 4. Analyze performance

I timed 100 searches for the last item in the large list and calculated the average time per search. The original run in IntelliJ's integrated terminal produced these results:

| Algorithm | Average time per search | Worst-case time |
| --- | ---: | --- |
| Linear search | 1.787271 ms | O(n) |
| Binary search | 0.001312 ms | O(log n) |

The timings do not include list creation and sorting and vary from run to run. They show the performance of this specific workload as opposed to a general speedup for all searches.

The linear search required to search all 100,000 items on the list to find the last item on the list or to find a item that was not on the list. The binary search required a maximum of 17 middle checks to find any item on a list of 100,000 items. This was because each step removed about half of the items on the list. The program measured the elapsed time for each search rather than counting the number of comparison checks. Both of the iterative search programs used O(1) additional search space.

The binary search relies on the values in the list being in ascending order. In order to use the binary search for searching an unsorted list, the list must first be sorted, which will take O(n log n) time. Then efficient index access is required for the O(log n) time binary search. My program requires the values in the list to be in sorted order before searching for a value in the list. This means that my program does not require scanning the entire list to verify that the list is in sorted order before searching for a value, which would take O(n) time.

### 5. Create a real-world search scenario

In this real world example, a technician was searching for the ID of equipment delivered in a delivery. The list of delivery IDs was `[118, 101, 130, 105, 124, 112]`. The linear search found ID `124` on the list of delivery IDs. A sorted copy of the list of delivery IDs was also created to simulate an organized inventory of equipment and the binary search was used to find the same ID.

Linear search is good for one lookup in a small list of items. Sorting the list first would be a waste of time. For repeated lookups in an organized list of items, binary search is better because the list of IDs is sorted. The returned index is the index in the list, not the original list. In this example, ID `124` was at index `4` in both the unsorted list of delivery IDs and the sorted copy of that list.

## How I ran the program

I ran the starter and completed implementation through IntelliJ's integrated terminal. From the `unit5_searching_analysis` folder, I used:

```bash
python3 unit5_discussion.py
```

The program used only Python's standard library. Its output showed the small dataset checks, large dataset checks and timings, eight edge cases, and equipment delivery example. All built-in checks passed.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

### Reflection

For this assignment, I decided to compare the efficiency of linear search versus binary search on lists of IT equipment IDs. The linear search methodically searches every single ID in a list. The binary search starts by searching the middle of the list and then narrows down the remaining elements based on the result of each search.

One of the main details that I included in the above explanation was the movement of the binary search boundaries past the middle index. I used mid + 1 and mid - 1 in order to prevent checking the same index over and over. This was tested by checking the first and last items of the list.

The time complexity of the worst case of a binary search on a sorted list of n elements is O(log n). This is because in each step, the search is narrowed down to half of the elements that were previously being searched for. For a linear search on a list of n elements, the worst case is O(n) because the search may have to go through every element in the list.

Linear search is still useful for checking a single ID in a small delivery of un-sorted equipment. There is no need to sort the list first. However, for repeated lookups of IDs in inventory, it is better to keep the list of IDs sorted, so that binary search can be used. Binary search will not work reliably on lists of un-sorted, comparable values.

## Reference

Python Software Foundation. (n.d.). *bisect — Array bisection algorithm*. Python documentation. https://docs.python.org/3/library/bisect.html

## Submission status

The implementation and README were committed to GitHub. The discussion was prepared for review; the initial post and peer responses were not submitted.
