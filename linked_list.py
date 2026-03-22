
from tracemalloc import start


class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        TODO:
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        TODO:
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        TODO:
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional) TODO:
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self, node=None, start=True):
        """
        TODO:
        - Use recursion to sum all node data in the list.
        - Consider a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        if start:
            node = self.head
        if not node:
            return 0
        return node.data + self.recursive_sum(node.next, False)

    def recursive_reverse(self):
        """
        TODO:
        - Reverse the list in-place using recursion.
        - Possible approach:
          1. Use a helper function that accepts 'prev' and 'current'.
          2. Base case: if current is None, return 'prev' (new head).
          3. Otherwise, swap pointers and recurse.
        - Update 'head' to the returned new head.
        """
        def _reverse(curr, prev):
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            return _reverse(next_node, curr)
        self.head = _reverse(self.head, None)

    def recursive_search(self, target, node=None, start=True):
        """
        TODO:
        - Return True if 'target' is found, otherwise False, using recursion.
        - Consider a helper function that:
          1. Returns False if the current node is None.
          2. Returns True if current node's data == target.
          3. Otherwise, recurse on the next node.
        """
        # 1. Handle starting point
        if start:
            node = self.head
        # 2. Base case: Not found
        if not node:
            return False
        # 3. Base case: Found
        if node.data == target:
            return True
        # 4. Recurse
        return self.recursive_search(target, node.next, False)

    def display(self):
        """
        TODO:
        - Print the contents of the list for debugging.
        - Traverse from 'head' and collect each node's data.
        - Format output as 'val -> val -> val -> None' or similar.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")
