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

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?


## Implementation

I modeled an ordered service-desk ticket list. I completed `insert_at` with `insert()`, `delete_at` with index validation and `pop()`, and `search_value` with a sequential loop. I preserved the starter TODO prompts and comments and added implementation comments below them.

I used nonnegative integer indexes for deletion. Invalid indexes returned `None` without modifying the list. Searches returned the first matching index, or `-1` when no value matched. Insertion followed Python's built-in `insert()` behavior, including clamping indexes outside the list boundaries.

## Running the program

```bash
python unit3_discussion.py
```

## Verification

I ran the completed program and checked insertion and deletion at the beginning, middle, and end. The search demonstration returned `1` for VPN and `-1` for a missing ticket. I checked empty-list insertion, deletion and searching; negative and out-of-range deletion indexes; a noninteger deletion index; deleting the only item; and duplicate searches. The service-desk example finished with `['Network outage', 'Printer', 'Email']` after removing the resolved VPN ticket.

## Performance

Beginning and middle insertions/deletions required shifting later references, taking O(n) time in the worst case. End insertion was amortized O(1); individual resizes could take O(n). Removing the final item was O(1). Linear searching took O(n) in the worst case. A linked list could avoid shifting when the necessary node references were already known, but locating a node still took O(n). Indexed access favored Python's array-based list.

## Reflection

The biggest takeaway from this assignment was that the position of an operation matters just as much as the operation itself. Adding an urgent ticket at the front shifted the later entries, while adding one at the end did not require that same shift. Working through the output made the difference easier to follow than just reading the time complexities.

One detail that needed care was the connection between searching and deleting. A missing search returned -1, but Python normally treats -1 as the final position in a list. I handled that by rejecting negative deletion indexes and checking the search result before removing a ticket. I also used separate data for the search demonstrations so earlier deletions would not change what those examples were testing.

For a small ticket list, these operations were straightforward. With thousands of pending tickets, repeated front insertions, middle deletions, and linear searches could add noticeable work. That is why I would choose the data structure based on how the application actually used its data.
