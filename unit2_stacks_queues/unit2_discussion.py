"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values go on top, so the newest value is removed first.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Inspect the top without changing the stack.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self._items


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New arrivals join the back; older arrivals stay at the front.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Inspect the oldest value without removing it.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self._items


def show_empty(label, operation):
    """Report an invalid removal or inspection without stopping the demo."""
    try:
        operation()
    except IndexError as error:
        print(f"{label}: {error}")


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK: UNDO NETWORK CHANGES ===")
    history = Stack()
    changes = ["Set hostname", "Configure VLAN", "Update route", "Apply ACL"]
    for change in changes:
        history.push(change)
        print(f"Recorded: {change}")
    print(f"Latest change (peek only): {history.peek()}")
    for expected in reversed(changes):
        actual = history.pop()
        assert actual == expected
        print(f"Undo: {actual}")
    assert history.is_empty()
    show_empty("Empty pop", history.pop)
    show_empty("Empty peek", history.peek)
    history.push("Enable port")
    assert history.peek() == "Enable port"
    assert history.pop() == "Enable port"
    assert history.is_empty()
    print("Single-item stack became empty: True")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE: IT SUPPORT TICKETS ===")
    tickets = Queue()
    requests = ["Password reset", "Printer issue", "VPN access", "Software install"]
    for request in requests:
        tickets.enqueue(request)
        print(f"Received: {request}")
    print(f"Next ticket (front only): {tickets.front()}")
    for expected in requests:
        actual = tickets.dequeue()
        assert actual == expected
        print(f"Serving: {actual}")
    assert tickets.is_empty()
    show_empty("Empty dequeue", tickets.dequeue)
    show_empty("Empty front", tickets.front)
    tickets.enqueue("Unlock account")
    assert tickets.front() == "Unlock account"
    assert tickets.dequeue() == "Unlock account"
    assert tickets.is_empty()
    print("Single-item queue became empty: True")

    # Reuse after emptying and duplicate values are valid operations.
    for structure, add, remove in (
        (Stack(), "push", "pop"), (Queue(), "enqueue", "dequeue")
    ):
        getattr(structure, add)("Repeat")
        getattr(structure, add)("Repeat")
        assert getattr(structure, remove)() == "Repeat"
        assert getattr(structure, remove)() == "Repeat"
        assert structure.is_empty()
        getattr(structure, add)("Reused")
        assert getattr(structure, remove)() == "Reused"
    print("Duplicate-value and reuse checks passed for both structures.")


if __name__ == "__main__":
    main()
