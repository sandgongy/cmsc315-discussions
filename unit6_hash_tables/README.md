# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Implementation

This is the model of a laptop checkout desk. Each laptop is assigned an asset tag and this is used as the key in the dictionary. The value for each laptop is the department that is borrowing the laptop. It is possible for two laptops to be checked out to the same department because each laptop has its own unique tag.

I added five records to the dictionary, looked up two tags, reassigned LT-104 from Training to Operations, and removed LT-123 when it was returned. I printed the dictionary before and after the reassignment and return of LT-123. The record count remained at five after the reassignment.

## Running the Program

I ran `python3 unit6_discussion.py` from this folder. The output showed these edge cases.

| Scenario | Observed result |
| --- | --- |
| Lookup of LT-999 | Reported that there was no active checkout. |
| Removal of LT-999 | Reported that there was no record to remove. |
| Reassignment of LT-999 | Rejected the update because the checkout did not exist. |
| Lookup in an empty dictionary | Returned the fallback message. |
| Duplicate checkout for LT-104 | Kept the existing Operations assignment. |

## Hashing and Collision Handling

This dictionary implementation hashes the tags to find the initial slot, with different tags ending up at the same slot. CPython uses open addressing and so will probe other slots if needed. Separate chaining would be different, with multiple entries in each bucket and searching within each bucket. Lookups, updates and removals are all O(1) average time, with insertion being amortized O(1) average time. However, many collisions can mean a single lookup takes O(n) worst case time. This is a separate issue to duplicate-tag checking (i.e. if the same key was entered twice).

## Reflection

I used laptop checkouts as a simple desktop support example. So, when someone calls about a laptop, I can look up the asset tag in our program and find out the department the laptop was assigned to. In the program, the asset tag is the dictionary key and the department the value.

The hardest part for me was figuring out how to handle both the first time a laptop was checked out as well as reassigning a laptop that was already checked out. Python uses the same syntax for both assignments. So, I added a membership check to prevent creating a new record for a mistyped tag during reassignment. I also tried to look up a tag in an empty dictionary and tried to remove a tag that was not in the dictionary.

The dictionary starts at a slot determined by a hash function. Two different tags can map to the same slot, so more slots may need to be searched for the value associated with a tag. This is why a lookup that normally takes O(1) time can take O(n) time in the worst case.