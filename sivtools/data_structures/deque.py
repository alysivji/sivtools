"""Linked list implementation of Deque"""


class Node:

    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        items = []

        curr_node = self.head
        while curr_node is not None:
            items.append(curr_node.value)
            curr_node = curr_node.next_node

        return str(items)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        """Get size of Deque"""

        count = 0
        curr_node = self.head
        while curr_node is not None:
            curr_node = curr_node.next_node
            count += 1

        return count

    def append_left(self, value):
        if self.head is None:
            node = Node(value, prev_node=None, next_node=None)
            self.head = node
            self.tail = node
        else:
            # get the current node that is at the top
            first_node = self.head

            # move around pointers so the head points to the new node
            new_node = Node(value, prev_node=None, next_node=first_node)
            first_node.prev_node = new_node
            self.head = new_node

    def append_right(self, value):
        if self.head is None:
            node = Node(value, prev_node=None, next_node=None)
            self.head = node
            self.tail = node
        else:
            # get the current node that is at the bottom
            last_node = self.tail

            # move around pointers so the tail points to the new node
            new_node = Node(value, prev_node=last_node, next_node=None)
            last_node.next_node = new_node
            self.tail = new_node

    def pop_left(self):
        print(self)
        if self.head is None:
            raise IndexError('retrieving item from empty deque')

        # move pointers around
        node_to_pop = self.head
        new_top = node_to_pop.next_node

        # if there is >1 element left, set prev_node to None
        if new_top is not None:
            new_top.prev_node = None
        else:
            # if there is only 1 element and we are popping it
            self.tail = None

        self.head = new_top

        return node_to_pop.value

    def pop_right(self):
        print(self)
        if self.tail is None:
            raise IndexError('retrieving item from empty deque')

        # move pointers around
        node_to_pop = self.tail
        new_bottom = node_to_pop.prev_node

        # if there is >1 element left, set next_node to None
        if new_bottom is not None:
            new_bottom.next_node = None
        else:
            # if there is only 1 element and we are popping it
            self.head = None

        self.tail = new_bottom

        return node_to_pop.value
