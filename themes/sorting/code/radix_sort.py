# Поразрядная сортировка (Radix sort, LSD — с младшего разряда)
# Время: O(d * (n + b)), d — число разрядов, b — основание системы счисления
# Память: O(n + b), устойчивая
# Идея: устойчиво раскладываем числа по последней цифре, потом по предпоследней и т. д.


def radix_sort(a, base=10):
    """Сортирует неотрицательные целые числа."""
    if not a:
        return []
    a = a[:]
    exp = 1                                 # 1, 10, 100, ... — текущий разряд
    while max(a) // exp > 0:
        buckets = [[] for _ in range(base)]
        for x in a:                         # раскладываем по цифре текущего разряда
            buckets[(x // exp) % base].append(x)
        a = [x for bucket in buckets for x in bucket]   # собираем, сохраняя порядок
        exp *= base
    return a


def radix_sort_verbose(a):
    a = a[:]
    exp = 1
    while max(a) // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a:
            buckets[(x // exp) % 10].append(x)
        a = [x for bucket in buckets for x in bucket]
        print(f"по разряду {exp:>3}: {a}")
        exp *= 10
    return a


if __name__ == "__main__":
    print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
    # [2, 24, 45, 66, 75, 90, 170, 802]

    radix_sort_verbose([170, 45, 75, 90, 802, 24, 2, 66])
    # по разряду   1: [170, 90, 802, 2, 24, 45, 75, 66]
    # по разряду  10: [802, 2, 24, 45, 66, 170, 75, 90]
    # по разряду 100: [2, 24, 45, 66, 75, 90, 170, 802]
