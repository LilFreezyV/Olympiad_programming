# Быстрая сортировка (Quick sort)
# Время: O(n log n) в среднем, O(n^2) в худшем (поэтому pivot выбираем случайно)
# Память: O(log n) на рекурсию (версия на месте), НЕустойчивая
import random
import sys
import time


def quick_sort(a):
    """Наглядная версия: делим на три списка. Проста, но создаёт много копий."""
    if len(a) <= 1:
        return a
    pivot = random.choice(a)
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def partition_sort(a, lo, hi, choose_pivot):
    """Сортировка на месте с разбиением Хоара; choose_pivot(lo, hi) возвращает индекс опорного."""
    if lo >= hi:
        return
    pivot = a[choose_pivot(lo, hi)]
    i, j = lo, hi
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    # теперь a[lo..j] <= pivot, a[i..hi] >= pivot
    partition_sort(a, lo, j, choose_pivot)
    partition_sort(a, i, hi, choose_pivot)


def quick_sort_inplace(a):
    """Правильная версия: случайный pivot."""
    partition_sort(a, 0, len(a) - 1, lambda lo, hi: random.randint(lo, hi))


def quick_sort_first_pivot(a):
    """ПЛОХАЯ версия: pivot всегда первый элемент. Только для сравнения."""
    partition_sort(a, 0, len(a) - 1, lambda lo, hi: lo)


if __name__ == "__main__":
    print(quick_sort([3, 6, 8, 10, 1, 2, 1]))   # [1, 1, 2, 3, 6, 8, 10]

    a = [3, 6, 8, 10, 1, 2, 1]
    quick_sort_inplace(a)
    print(a)                                     # [1, 1, 2, 3, 6, 8, 10]

    # На уже отсортированном массиве первый элемент — всегда минимум:
    # разбиение даёт части 0 и n-1, глубина рекурсии ~n, время O(n^2).
    # При n = 3000 плохая версия на Windows просто роняет Python (переполнение стека)
    sys.setrecursionlimit(10000)
    n = 900
    for sort in (quick_sort_inplace, quick_sort_first_pivot):
        a = list(range(n))
        t = time.perf_counter()
        sort(a)
        print(f"{sort.__name__:>24}: {time.perf_counter() - t:.3f} с")
