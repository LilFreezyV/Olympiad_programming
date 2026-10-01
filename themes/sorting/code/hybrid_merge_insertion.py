# Гибрид: сортировка слиянием + вставками
# Большие куски делим пополам, как в merge sort,
# а куски длиной <= THRESHOLD досортировываем вставками.
# Время: O(n log n), память O(n), устойчивая
import random
import time

THRESHOLD = 16


def insertion_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(a):
    """Чистая сортировка слиянием — делит до кусков длины 1."""
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def hybrid_merge_sort(a, threshold=THRESHOLD):
    """Гибрид: маленькие куски сортируем вставками."""
    if len(a) <= threshold:
        a = a[:]
        insertion_sort(a)
        return a
    mid = len(a) // 2
    return merge(hybrid_merge_sort(a[:mid], threshold),
                 hybrid_merge_sort(a[mid:], threshold))


if __name__ == "__main__":
    print(hybrid_merge_sort([5, 2, 9, 1, 6, 3, 8, 7, 4, 0] * 3))

    # Сравним время для разных порогов: 1 — это чистый merge sort
    n = 50_000
    data = [random.randint(0, 10**9) for _ in range(n)]
    print(f"n = {n}")
    for threshold in (1, 4, 8, 16, 32, 64, 256):
        t = time.perf_counter()
        result = hybrid_merge_sort(data, threshold)
        dt = time.perf_counter() - t
        assert result == sorted(data)
        print(f"  порог {threshold:>3}: {dt:.3f} с")
    # Обычно лучший порог — где-то 8..32. При очень большом пороге
    # квадратичные вставки снова начинают тормозить.
