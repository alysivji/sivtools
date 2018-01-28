"""Linked list implementation of Stack"""


class Node:

    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        count = 0
        curr_node = self.head
        while curr_node is not None:
            curr_node = curr_node.next_node
            count += 1

        return count

    def push(self, value):
        """Push item into stack"""

        # point to where head is pointing
        next_node = self.head
        node = Node(value, next_node)

        self.head = node

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack')

        node_to_pop = self.head
        self.head = node_to_pop.next_node

        return node_to_pop.value
