class MinHeap:
    def __init__(self):
        self.heap = []  # внутренний список

    # ---------- Вспомогательные методы ----------
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # ---------- Просеивание вверх ----------
    def _sift_up(self, i):
        """
        Поднимает элемент вверх, пока он меньше родителя.
        Используется после добавления в конец.
        """
        while i > 0:
            p = self._parent(i)
            if self.heap[p] <= self.heap[i]:
                break  # свойство кучи выполнено
            self._swap(i, p)
            i = p

    # ---------- Просеивание вниз ----------
    def _sift_down(self, i):
        """
        Опускает элемент вниз, пока он больше любого из потомков.
        Используется после удаления корня.
        """
        n = len(self.heap)
        while True:
            smallest = i
            l = self._left(i)
            r = self._right(i)

            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest == i:
                break  # элемент на месте
            self._swap(i, smallest)
            i = smallest

    # ---------- Публичные операции ----------
    def push(self, value):
        """Добавить элемент. O(log n)."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Извлечь минимум. O(log n)."""
        if not self.heap:
            return None
        root = self.heap[0]

        last = self.heap.pop()       # убираем последний
        if self.heap:                # если ещё есть элементы
            self.heap[0] = last      # ставим его в корень
            self._sift_down(0)       # и просеиваем вниз

        return root

    def peek(self):
        """Посмотреть минимум без удаления. O(1)."""
        return self.heap[0] if self.heap else None

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return len(self.heap) > 0