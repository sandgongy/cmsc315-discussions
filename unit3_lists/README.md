# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

Add your reflection to your initial post on the discussion board in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?


## Implementation

I implemented an ordered service-desk ticket list. This included implementing the `insert_at` function using the `insert()` method, the `delete_at` function using index validation and the `pop()` method, and the `search_value` function using a sequential loop. I left the TODO prompts and comments as is, and added my own implementation comments below them.

For the deletion operations I used nonnegative integer indexes, returning None for invalid indexes and not modifying the list. For the searches I returned the first index matching the search value, or -1 if no value was found. For the insertion operations I used Python’s built-in insert() method, so for example if the index given was greater than the length of the list then it would be clamped to the end of the list.

## Running the program

```bash
python unit3_discussion.py
```

## Verification

The completed code was tested by inserting/deleting from the beginning, middle and end of the list. A simple search was also tested which returned 1 for ‘VPN’ and -1 for ‘Printer’ as expected. I also tested the empty list for insertion, deletion and searching. Additionally I tested for negative and out of range index for deletion, non integer index for deletion, deleting the only item in the list and searching for a value that appears multiple times in the list. The final list after the service-desk example was ‘['Network outage', 'Printer', 'Email']’ after the VPN ticket was resolved.

## Performance

The insertion and deletion of elements at the beginning or the middle of the list require the shifting of all the other elements in the list. Thus, the worst case running time of these operations is O(n). However, the insertion of an element at the end of the list is amortized O(1). The removal of the last element in the list is also O(1). The search for an element in the list is done in linear time, i.e. in the worst case the running time is O(n). A linked list would allow to insert and remove elements at any position in the list in constant time, given that the node where the operation is to take place is already known. However, finding such a node in the list takes O(n) in the worst case. Therefore, for an application that requires access to elements in the list by their index, a list implemented as an array is the best choice.

## Reflection

This assignment really helped to drive home the point that where we add/remove/search for items in a list can be as important as what we are adding/removing/searching for. For example, adding an urgent ticket at the front of the list will cause all other tickets to be shifted, but adding an urgent ticket at the end of the list will not require any shifting.

One thing that was a bit tricky to implement was searching for a ticket and then deleting it. The search returns the index of the ticket if found, or -1 if not found. Since -1 can be treated as the last element in a list, I needed to reject any negative index for deletion. Also, the search demonstrations needed to be done with separate data so that earlier deletions did not affect the results of the search demonstrations.

This assignment was good for learning how to implement a list of service desk tickets but the operations on a list of service desk tickets would be very different with thousands of pending tickets. For example, many front insertions, many middle deletions, and many linear searches would be very slow. I would choose a different data structure to implement service desk tickets based on how the list of tickets is used.
