# Сортировка слиянием (Merge sort)
# Время: всегда O(n log n)
# Память: O(n), устойчивая


def merge(left, right):
    """Слияние двух отсортированных списков двумя указателями."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:             # <= сохраняет устойчивость
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])                 # один из хвостов пуст,
    result.extend(right[j:])                # второй просто дописываем
    return result


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def sort_and_count(a):
    """Сортирует и считает число инверсий (пар i < j, где a[i] > a[j]) за O(n log n)."""
    if len(a) <= 1:
        return a, 0
    mid = len(a) // 2
    left, inv_l = sort_and_count(a[:mid])
    right, inv_r = sort_and_count(a[mid:])

    result = []
    inv = inv_l + inv_r
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inv += len(left) - i            # right[j] меньше всех left[i:]
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv


if __name__ == "__main__":
    print(merge([1, 4, 7], [2, 3, 8]))          # [1, 2, 3, 4, 7, 8]
    print(merge_sort([5, 2, 9, 1, 6, 3]))       # [1, 2, 3, 5, 6, 9]

    print(sort_and_count([3, 1, 2]))            # ([1, 2, 3], 2)
    print(sort_and_count([5, 4, 3, 2, 1])[1])   # 10
