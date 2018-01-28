"""Implementation of Python list using Linked List"""

from collections import abc
import numbers


class Node(object):
    """Node that holds data and a link to the next node"""

    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_

    def __repr__(self):  # pragma: no cover
        return 'Node: ' + str(self.data)


class LinkedList(object):
    """List implemented via Linked List"""

    # TODO: extend, remove, clear, sort, reverse, copy, __getitem__

    def __init__(self, items=None):
        self._head = None
        self.length = 0

        if items is not None:
            if isinstance(items, numbers.Number) or isinstance(items, str):
                self.append(items)
            elif isinstance(items, abc.Iterable):
                if items is not None:
                    for item in items:
                        self.append(item)
            else:
                raise TypeError

    def append(self, item):
        """Add item to back of list"""
        node_to_insert = Node(item)

        if self.is_empty():
            self._head = node_to_insert
        else:
            last_node = self.tail
            last_node.next_ = node_to_insert
        self.tail = node_to_insert

        self.length += 1

    def index(self, value):
        """Return the index of the first item in value"""
        curr = self._head
        counter = 0

        while curr is not None:
            if curr.data == value:
                return counter
            curr = curr.next_
            counter += 1
        raise ValueError('{0} is not in list'.format(value))

    def insert(self, index, value):
        """Inserts value at index"""
        if index == 0:
            node_to_insert = Node(value, self._head.next_)
            self._head = node_to_insert
        elif index < 0:
            self.insert(0, value)
        elif index >= len(self):
            self.append(value)
        else:
            curr = self._head
            counter = 0

            while counter < index:
                if counter + 1 == index:
                    node_to_insert = Node(value, curr.next_)
                    curr.next_ = node_to_insert
                curr = curr.next_
                counter += 1

    def is_empty(self):
        """Checks to see if list is empty"""
        return len(self) == 0

    def pop(self, index=None):
        """Pop element at index from list and return"""
        # default action is to pop last element
        if index is None:
            index = self.length - 1

        if self._head is None:
            raise IndexError("pop from empty list")
        if index > self.length - 1:
            raise IndexError("pop index out of range")

        if index == 0 or len(self) == 1:
            item_to_pop = self._head
            self._head = item_to_pop.next_
        else:
            prev_node = self._head
            curr_node = self._head.next_
            counter = 1

            while counter <= index:
                if counter == index:
                    item_to_pop = curr_node
                    prev_node.next_ = curr_node.next_
                counter += 1
                curr_node = curr_node.next_
                prev_node = prev_node.next_

        self.length -= 1
        return item_to_pop.data

    def __iter__(self):
        curr = self._head
        while curr is not None:
            yield curr.data
            curr = curr.next_

    def __len__(self):
        return self.length

    def __repr__(self):
        return str(list(self))
