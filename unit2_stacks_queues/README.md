# Unit 2: Stacks and Queues
Joel Sandjong

For this assignment, I completed the Stack and Queue classes and used network changes and IT support tickets as examples. I kept the original TODO comments and added explanations beside the operations.

## What I implemented
I used a Python list for the stack. push() added an item to the end, pop() removed the newest item, and peek() returned that item without removing it. My network-change example recorded four changes and undid them in reverse order: Apply ACL, Update route, Configure VLAN, then Set hostname.

I used collections.deque for the queue. enqueue() added a ticket to the back, dequeue() removed the oldest ticket with popleft(), and front() inspected the next ticket. The tickets were served in their arrival order: Password reset, Printer issue, VPN access, then Software install.

I chose to raise IndexError with a clear message for empty removals and inspections. The demo caught those errors and printed the messages so it continued running. This also kept an empty structure distinguishable from a stored value.

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
The list's end append and pop operations took amortized O(1) time. The deque's append and popleft operations took O(1) time, avoiding the O(n) shifts of list.pop(0). Both structures required O(n) space for n stored references, plus the memory of the stored values. More items required more memory; exact bytes depended on the values and container overhead. I did not impose a fixed capacity.

## Reflection
This assignment helped me understand why the removal order matters as much as the values being stored. I used network changes for the stack because undoing the latest change first made sense. If a new access rule caused a problem, that would be the first change I would want to reverse. The queue worked differently: support tickets were handled in the order they arrived.

The part I paid the most attention to was handling an empty structure. Calling pop or popleft without a check would have stopped the program with an error. I added explicit checks and caught the errors in the demonstration so the output showed what happened and continued.

I also checked that peek and front did not remove anything by checking the full removal order afterward. Testing one-item structures helped confirm that the empty state was correct after the last removal. Seeing both demonstrations run made LIFO and FIFO easier to connect to everyday software behavior.
