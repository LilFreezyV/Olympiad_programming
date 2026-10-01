# Сортировка выбором (Selection sort)
# Время: всегда O(n^2) сравнений, но не больше n - 1 обменов
# Память: O(1), НЕустойчивая


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        m = i                               # индекс минимума среди a[i:]
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]             # ставим минимум на позицию i


def selection_sort_verbose(a):
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
        print(f"шаг {i + 1}: минимум {a[i]} → позиция {i}: {a}")


if __name__ == "__main__":
    a = [64, 25, 12, 22, 11]
    selection_sort(a)
    print(a)                                # [11, 12, 22, 25, 64]

    selection_sort_verbose([64, 25, 12, 22, 11])

    # Неустойчивость: сортируем пары только по первому элементу
    pairs = [(5, "a"), (5, "b"), (1, "c")]
    n = len(pairs)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if pairs[j][0] < pairs[m][0]:
                m = j
        pairs[i], pairs[m] = pairs[m], pairs[i]
    print(pairs)                            # [(1, 'c'), (5, 'b'), (5, 'a')] — 'a' и 'b' поменялись
