a = [2, 3, 5, 6, 4, 5, 6]


# ---------- Просеивание вверх ----------
def sift_up(i):
    """Поднимает элемент вверх, пока он больше родителя."""
    while i > 0:
        p = (i - 1) // 2
        if a[i] <= a[p]:
            break
        a[i], a[p] = a[p], a[i]
        i = p


# ---------- Просеивание вниз ----------
def sift_down(i, size=None):
    """Опускает элемент вниз, пока он меньше любого из потомков."""
    if size is None:
        size = len(a)
    while True:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size and a[l] > a[largest]:
            largest = l
        if r < size and a[r] > a[largest]:
            largest = r
        if largest == i:
            break
        a[i], a[largest] = a[largest], a[i]
        i = largest


# ---------- Добавление ----------
def add(x):
    """Добавить элемент в кучу. O(log n)."""
    a.append(x)
    sift_up(len(a) - 1)


# ---------- Извлечение максимума ----------
def get():
    """Извлечь максимум из кучи. O(log n)."""
    if not a:
        return None
    root = a[0]
    last = a.pop()
    if a:
        a[0] = last
        sift_down(0)
    return root


# ---------- Просмотр максимума ----------
def peek():
    """Посмотреть максимум без удаления. O(1)."""
    return a[0] if a else None


# ---------- Построение кучи из массива ----------
def heapify():
    """Превратить массив a в макс-кучу. O(n)."""
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)


# ---------- Проверка, является ли массив кучей ----------
def is_heap():
    """Проверить, что массив a удовлетворяет свойству макс-кучи."""
    n = len(a)
    for i in range(n):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[l] > a[i]:
            return False
        if r < n and a[r] > a[i]:
            return False
    return True


# ---------- Вывод кучи в виде дерева (для отладки) ----------
def print_heap():
    """Печатает массив и его структуру."""
    print("Массив:", a)
    n = len(a)
    if n == 0:
        return
    level = 0
    count = 0
    for i in range(n):
        print(a[i], end=" ")
        count += 1
        if count == 2 ** level:
            print()
            level += 1
            count = 0
    print()


# ---------- ТЕСТЫ ----------
if __name__ == "__main__":
    print("Исходный массив:", a)
    heapify()
    print("После heapify:  ", a)
    print("Это куча?", is_heap())

    add(10)
    print("После add(10):  ", a)
    print("Это куча?", is_heap())

    add(1)
    print("После add(1):   ", a)
    print("Это куча?", is_heap())

    print("peek():", peek())

    print("get():", get())
    print("После get():    ", a)
    print("Это куча?", is_heap())

    print("get():", get())
    print("После get():    ", a)
    print("Это куча?", is_heap())

    # Извлечём всё — получим отсортированный по убыванию ряд
    print("\nИзвлекаем всё по порядку:")
    while a:
        print(get(), end=" ")
    print()