# Пирамидальная сортировка (Heap sort)
# Время: всегда O(n log n)
# Память: O(1) в версии на месте, НЕустойчивая
# Подробно про кучу — themes/heap/theory/theory.md
import heapq


def sift_down(a, i, size):
    """Опускает a[i] вниз в max-куче из первых size элементов."""
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


def heap_sort(a):
    n = len(a)
    # 1. Строим max-кучу за O(n)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(a, i, n)
    # 2. Максимум (корень) меняем с последним элементом и «укорачиваем» кучу
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end)


def heap_sort_heapq(a):
    """Короткая версия на heapq (min-куча), возвращает новый список."""
    h = a[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


if __name__ == "__main__":
    a = [12, 11, 13, 5, 6, 7]
    heap_sort(a)
    print(a)                                        # [5, 6, 7, 11, 12, 13]

    print(heap_sort_heapq([12, 11, 13, 5, 6, 7]))   # [5, 6, 7, 11, 12, 13]
