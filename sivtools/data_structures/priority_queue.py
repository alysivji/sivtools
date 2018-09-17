import heapq


class MinHeap:
    """Python wrapper around standard library heapq"""

    def __init__(self, iterable=list()):
        self._h = []
        for item in iterable:
            self.heappush(item)

    def __repr__(self):
        return repr(self._h)

    def __getitem__(self, key):
        return self._h[key]

    def __len__(self):
        return len(self._h)

    def __eq__(self, right):
        return self._h == right

    def pop(self):
        return heapq.heappop(self._h)

    def push(self, item):
        heapq.heappush(self._h, item)

    def pushpop(self, item):
        """Push first, then pop"""
        return heapq.heappushpop(self._h, item)

    def replace(self, item):
        """Pop first, then push"""
        return heapq.heapreplace(self._h, item)
