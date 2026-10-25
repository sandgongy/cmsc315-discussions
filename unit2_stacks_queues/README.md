# Unit 2: Stacks and Queues
Joel Sandjong

For this assignment, I completed the Stack and Queue classes and used network changes and IT support tickets as examples. I maintained all the original TODO comments, with explanations next to the operations.

## What I implemented
Implemented a Python list for the stack: push() inserted an item into the end, pop() took out the most recently added item, and peek() returned the most recent item without removing it. My network-change example recorded four changes and undid them in reverse order: Apply ACL, Update route, Configure VLAN, then Set hostname.

I used collections.deque for the queue. enqueue() added a ticket to the back, dequeue() removed the oldest ticket with popleft(), and front() inspected the next ticket. The tickets were served in their arrival order: Password reset, Printer issue, VPN access, then Software install.

I decided to raise IndexError with a nice message for empty removals and inspections. The demo caught those errors and printed the messages so it continued running. This also made it possible to keep an empty structure distinguishable from a stored value.

## How I checked it
I ran the program with Python 3:
```text
python unit2_discussion.py
```

The assertions checked the complete LIFO and FIFO sequences, non-removing inspections, and empty state after all removals. I also checked single-item structures, duplicate values, and reuse after emptying. Empty pop, peek, dequeue, and front operations printed their error messages. The run finished with:
```text
Single-item stack became empty: True
Single-item queue became empty: True
Duplicate-value and reuse checks passed for both structures.
```

## Efficiency and memory
The list's end append and pop operations took amortized O(1) time. It allowed append and popleft in O(1) time without the O(n) list.pop(0) shift. Both structures required O(n) space for n stored references, plus the memory of the stored values. The larger the number of items, the more memory it needed, with exact bytes being dependent on the values and container overhead. I didn't set a specific capacity.

## Reflection
This assignment gave me a real sense of how important the removal order is in addition to the values being removed. I used network changes for the stack because undoing the latest change first made sense. If something went wrong due to a new access rule, that would be the first rule to go back to its original state. The queue was different, supporting tickets were processed as they came in.

I'm particularly interested in what I did with the empty building. If no check had been made, an error would have terminated the program when pop or popleft was called. I put in the checks and caught the mistakes in the demo so that the output had what was going on and it then continued.

I also checked that peek and front did not remove anything by checking the full removal order afterward. Testing of one item structures was useful in checking whether the empty state was correct after the last removal. Both LIFO and FIFO were easier to relate to common software behavior after seeing both demonstrations.
