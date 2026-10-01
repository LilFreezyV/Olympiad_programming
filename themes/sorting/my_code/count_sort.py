def counting_sort(inp, k):
    """
    Сортировка подсчётом для чисел в диапазоне от 1 до k.

    inp — список целых чисел, каждое в [1, k]
    k   — верхняя граница диапазона (максимально возможное значение)
    """
    a = [0] * k
    for x in inp:
        a[x - 1] += 1

    result = []
    for el in range(k):
        result.extend([el + 1] * a[el])
    return result


inp = [4, 5, 6, 3, 2, 1, 3, 4, 5, 6]
print(inp)
print(counting_sort(inp, k=6))
