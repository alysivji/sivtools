# use hypothesis

import heapq

from sivtools.data_structures import MinHeap


def test_empty_heap():
    min_heap = MinHeap()
    h = []

    assert min_heap == h
    assert h == min_heap


def test_creating_heap():
    item1 = (1, "item1")
    item2 = (2, "item2")
    min_heap = MinHeap()
    min_heap.push(item1)
    min_heap.push(item2)

    h = []
    heapq.heappush(h, item1)
    heapq.heappush(h, item2)

    assert min_heap == h
    assert h == min_heap


def test_heap_push_pop_separately():
    item1 = (1, "item1")
    item2 = (2, "item2")
    min_heap = MinHeap()
    min_heap.push(item1)
    min_heap.push(item2)

    h = []
    heapq.heappush(h, item1)
    heapq.heappush(h, item2)

    while h:
        assert min_heap.pop() == heapq.heappop(h)


def test_heap_pushpop_operation():
    item1 = (1, "item1")
    item2 = (2, "item2")
    min_heap = MinHeap()
    min_heap.push(item1)
    min_heap.push(item2)

    h = []
    heapq.heappush(h, item1)
    heapq.heappush(h, item2)

    new_item = (0, "item0")
    min_heap_popped = min_heap.pushpop(new_item)
    heapq_popped = heapq.heappushpop(h, new_item)

    assert min_heap_popped == heapq_popped == new_item
    assert min_heap == h


def test_heap_replace_operation():
    item1 = (1, "item1")
    item2 = (2, "item2")
    min_heap = MinHeap()
    min_heap.push(item1)
    min_heap.push(item2)

    h = []
    heapq.heappush(h, item1)
    heapq.heappush(h, item2)

    new_item = (0, "item0")
    min_heap_popped = min_heap.replace(new_item)
    heapq_popped = heapq.heapreplace(h, new_item)

    assert min_heap_popped == heapq_popped != new_item
    assert min_heap == h
