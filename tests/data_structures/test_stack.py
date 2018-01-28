from sivtools.data_structures import Stack
import pytest


def test_create_empty_stack():
    stack = Stack()

    assert stack.size() == 0
    assert stack.is_empty() is True
    assert stack.head is None


def test_stack_push():
    stack = Stack()
    stack.push(5)

    assert stack.size() == 1
    assert stack.is_empty() is False


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    item = stack.pop()

    assert item == 3
    assert stack.size() == 2


def test_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_fill_stack_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    item1 = stack.pop()
    item2 = stack.pop()

    assert item1 == 2
    assert item2 == 1
    assert stack.is_empty() is True
