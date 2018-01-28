from sivtools.data_structures import Deque
import pytest


def test_create_empty_deque():
    deque = Deque()

    assert deque.head is None
    assert deque.tail is None


def test_deque_append_left():
    deque = Deque()
    deque.append_left(0)
    deque.append_left(1)

    assert deque.size() == 2


def test_deque_append_right():
    deque = Deque()
    deque.append_right(0)
    deque.append_right(1)

    assert deque.size() == 2


def test_deque_pop_left():
    deque = Deque()
    deque.append_left(0)
    deque.append_left(1)
    item = deque.pop_left()

    assert item == 1
    assert deque.size() == 1


def test_deque_pop_left_multiple():
    deque = Deque()
    deque.append_left(0)
    deque.append_left(1)
    item1 = deque.pop_left()
    item2 = deque.pop_left()

    assert item1 == 1
    assert item2 == 0
    assert deque.is_empty() is True


def test_deque_pop_left_empty():
    deque = Deque()

    with pytest.raises(IndexError):
        deque.pop_left()


def test_deque_append_right_pop_left():
    deque = Deque()
    deque.append_right(0)
    deque.append_right(1)
    item0 = deque.pop_left()
    item1 = deque.pop_left()

    assert item0 == 0
    assert item1 == 1
    assert deque.is_empty() is True


def test_deque_pop_right():
    deque = Deque()
    deque.append_left(0)
    deque.append_left(1)
    item = deque.pop_right()
    item2 = deque.pop_right()

    assert item == 0
    assert item2 == 1
    assert deque.is_empty() is True


def test_deque_try_multiple_things():
    deque = Deque()
    deque.append_left(0)
    deque.append_left(1)
    # [1, 0]
    deque.append_right(3)
    deque.append_right(4)
    # [1, 0, 3, 4]

    item1 = deque.pop_left()
    item2 = deque.pop_right()

    assert item1 == 1
    assert item2 == 4

    item3 = deque.pop_right()
    item4 = deque.pop_right()

    assert item3 == 3
    assert item4 == 0

    assert deque.is_empty() is True

    with pytest.raises(IndexError):
        deque.pop_left()

    with pytest.raises(IndexError):
        deque.pop_right()
