# Сортировка подсчётом (Counting sort)
# Время: O(n + k), где k — размер диапазона значений
# Память: O(k), устойчивая (версия с префиксными суммами)
# Работает только для целых чисел из небольшого диапазона


def counting_sort(a, k):
    """Все элементы a — целые числа из [0, k)."""
    cnt = [0] * k
    for x in a:
        cnt[x] += 1
    result = []
    for value in range(k):
        result.extend([value] * cnt[value])
    return result


def counting_sort_range(a):
    """Произвольные целые числа (в т.ч. отрицательные): сдвигаем на минимум."""
    if not a:
        return []
    lo, hi = min(a), max(a)
    cnt = [0] * (hi - lo + 1)
    for x in a:
        cnt[x - lo] += 1
    result = []
    for i, c in enumerate(cnt):
        result.extend([i + lo] * c)
    return result


def counting_sort_by_key(items, key, k):
    """Устойчиво сортирует объекты по целому ключу key(item) из [0, k)."""
    cnt = [0] * k
    for it in items:
        cnt[key(it)] += 1
    start = [0] * k                         # start[v] — первая позиция для ключа v
    for v in range(1, k):
        start[v] = start[v - 1] + cnt[v - 1]
    result = [None] * len(items)
    for it in items:                        # идём в исходном порядке → устойчиво
        v = key(it)
        result[start[v]] = it
        start[v] += 1
    return result


if __name__ == "__main__":
    print(counting_sort([3, 1, 4, 1, 5, 1, 3], 6))       # [1, 1, 1, 3, 3, 4, 5]
    print(counting_sort_range([3, -2, 0, -2, 7]))        # [-2, -2, 0, 3, 7]

    pupils = [("Аня", 5), ("Боря", 4), ("Вика", 5), ("Гоша", 4)]
    print(counting_sort_by_key(pupils, key=lambda p: p[1], k=6))
    # [('Боря', 4), ('Гоша', 4), ('Аня', 5), ('Вика', 5)]
