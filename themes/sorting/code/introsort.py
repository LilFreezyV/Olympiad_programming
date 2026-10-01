# Интроспективная сортировка (Introsort) — так устроен std::sort в C++
# 1. Основа — быстрая сортировка.
# 2. Если глубина рекурсии превысила 2 * log2(n) — значит, pivot выбирается
#    неудачно и грозит O(n^2). Этот кусок досортировываем пирамидальной (heap sort).
# 3. Куски длиной <= SMALL досортировываем вставками.
# Время: O(n log n) ВСЕГДА, память O(log n), НЕустойчивая
import math
import random
import time

SMALL = 16
stats = {"heap_sort": 0, "insertion": 0}   # сколько раз сработал каждый «запасной» алгоритм


def insertion_sort_range(a, lo, hi):
    """Сортирует вставками a[lo..hi] включительно."""
    for i in range(lo + 1, hi + 1):
        x = a[i]
        j = i - 1
        while j >= lo and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


def heap_sort_range(a, lo, hi):
    """Пирамидальная сортировка a[lo..hi]: куча строится со сдвигом на lo."""
    n = hi - lo + 1

    def sift_down(i, size):
        while True:
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < size and a[lo + l] > a[lo + largest]:
                largest = l
            if r < size and a[lo + r] > a[lo + largest]:
                largest = r
            if largest == i:
                return
            a[lo + i], a[lo + largest] = a[lo + largest], a[lo + i]
            i = largest

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)
    for end in range(n - 1, 0, -1):
        a[lo], a[lo + end] = a[lo + end], a[lo]
        sift_down(0, end)


def median_of_three(a, lo, hi):
    """Индекс медианы из a[lo], a[mid], a[hi] — так выбирает pivot std::sort."""
    mid = (lo + hi) // 2
    x, y, z = a[lo], a[mid], a[hi]
    if x <= y <= z or z <= y <= x:
        return mid
    if y <= x <= z or z <= x <= y:
        return lo
    return hi


def first_element(a, lo, hi):
    """ПЛОХОЙ выбор pivot — только чтобы показать, как introsort спасает ситуацию."""
    return lo


def _introsort(a, lo, hi, depth, choose_pivot):
    if hi - lo + 1 <= SMALL:
        stats["insertion"] += 1
        insertion_sort_range(a, lo, hi)
        return
    if depth == 0:                              # рекурсия слишком глубокая
        stats["heap_sort"] += 1
        heap_sort_range(a, lo, hi)
        return
    pivot = a[choose_pivot(a, lo, hi)]
    i, j = lo, hi                               # разбиение Хоара, как в quick_sort.py
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    _introsort(a, lo, j, depth - 1, choose_pivot)
    _introsort(a, i, hi, depth - 1, choose_pivot)


def introsort(a, choose_pivot=median_of_three):
    if len(a) < 2:
        return
    max_depth = 2 * int(math.log2(len(a)))
    _introsort(a, 0, len(a) - 1, max_depth, choose_pivot)


if __name__ == "__main__":
    a = [random.randint(0, 99) for _ in range(30)]
    introsort(a)
    print(a)

    # Плохой pivot (первый элемент) на отсортированном массиве.
    # Обычный quicksort здесь работает за O(n^2) и при n = 3000 роняет Python
    # (см. quick_sort.py). Introsort замечает, что рекурсия слишком глубокая,
    # и переключается на heap sort.
    n = 100_000
    a = list(range(n))
    stats.update(heap_sort=0, insertion=0)
    t = time.perf_counter()
    introsort(a, choose_pivot=first_element)
    print(f"\nплохой pivot, отсортированный массив, n = {n}: {time.perf_counter() - t:.3f} с")
    print(f"  максимальная глубина рекурсии: {2 * int(math.log2(n))}")
    print(f"  переключений на heap sort: {stats['heap_sort']}")
    assert a == list(range(n))

    # Нормальный режим: медиана из трёх, случайные данные
    a = [random.randint(0, 10**9) for _ in range(n)]
    stats.update(heap_sort=0, insertion=0)
    t = time.perf_counter()
    introsort(a)
    print(f"\nмедиана из трёх, случайный массив, n = {n}: {time.perf_counter() - t:.3f} с")
    print(f"  переключений на heap sort: {stats['heap_sort']}")
    print(f"  кусков досортировано вставками: {stats['insertion']}")
    assert a == sorted(a)
