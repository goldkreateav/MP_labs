class PriorityQueue:
    def __init__(self):
        self._container = []

    def empty(self):
        return len(self._container) == 0

    def size(self):
        return len(self._container)

    def push(self, item):
        self._container.append(item)
        self._sift_up(len(self._container) - 1)

    def pop(self):
        if self.empty():
            raise IndexError("pop from an empty priority queue")
        self._swap(0, len(self._container) - 1)
        item = self._container.pop()
        self._sift_down(0)
        return item

    def top(self):
        if self.empty():
            raise IndexError("top from an empty priority queue")
        return self._container[0]

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self._container[idx] > self._container[parent]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        child = 2 * idx + 1
        if child < len(self._container):
            if child + 1 < len(self._container) and self._container[child + 1] > self._container[child]:
                child += 1
            if self._container[child] > self._container[idx]:
                self._swap(child, idx)
                self._sift_down(child)

    def _swap(self, i, j):
        self._container[i], self._container[j] = self._container[j], self._container[i]

