import pytest

from sivtools.data_structures import LinkedList


def test_create_empty_list():
    test_list = LinkedList()
    assert len(test_list) == 0


def test_create_list_with_elements():
    initial_list = [0, 1, 2, 3, 4, 5]
    test_list = LinkedList(initial_list)

    assert len(test_list) == len(initial_list)
    # checks if they are in the same order
    assert str(test_list) == str(initial_list)


def test_create_list_with_single_element():
    test_list = LinkedList(0)
    assert len(test_list) == 1

    test_list_str = LinkedList('item')
    assert len(test_list_str) == 1


def test_create_with_invalid_argument():
    with pytest.raises(TypeError):
        LinkedList(len)


def test_list_index():
    initial_list = [0, 1, 2, 3, 4, 5, 3]
    test_list = LinkedList(initial_list)

    assert test_list.index(0) == 0
    assert test_list.index(1) == 1
    assert test_list.index(2) == 2
    assert test_list.index(3) == 3
    assert test_list.index(4) == 4
    assert test_list.index(5) == 5

    with pytest.raises(ValueError):
        test_list.index(12)


def test_list_insert():
    # Test inserting at front or -1
    initial_list = [0, 1, 2]
    test_list = LinkedList(initial_list)
    test_list.insert(0, 'test')
    assert test_list.index('test') == 0
    test_list.insert(-1, 'test_negative_number')
    assert test_list.index('test_negative_number') == 0

    # Insert at end
    test_list_2 = LinkedList(initial_list)
    test_list_2.insert(10, 3)
    assert test_list_2.index(3) == 3
    test_list_2.insert(4, 'test')

    # Insert in middle
    test_list_3 = LinkedList(initial_list)
    test_list_3.insert(1, 'test')
    assert test_list_3.index('test') == 1


def test_pop_empty_list():
    test_list = LinkedList()
    with pytest.raises(IndexError):
        test_list.pop()


def test_pop_beyond_range():
    test_list = LinkedList([0, 1])
    with pytest.raises(IndexError):
        test_list.pop(10)


def test_pop_list_with_single_item():
    initial_list = [0]
    test_list = LinkedList(initial_list)
    assert test_list.pop() == 0
    assert len(test_list) == 0


def test_pop_list_with_multiple_elements():
    initial_list = [0, 1, 2, 4, 5]
    test_list = LinkedList(initial_list)

    # pop in middle
    assert test_list.pop(1) == 1
    assert len(test_list) == 4

    # pop from end
    assert test_list.pop() == 5
    assert len(test_list) == 3

    # pop rest of items
    assert test_list.pop() == 4
    assert len(test_list) == 2

    # pop rest of items
    assert test_list.pop() == 2
    assert len(test_list) == 1

    # pop rest of items
    assert test_list.pop() == 0
    assert len(test_list) == 0

    with pytest.raises(IndexError):
        assert test_list.pop()
