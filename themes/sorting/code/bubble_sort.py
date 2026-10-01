# Сортировка пузырьком (Bubble sort)
# Время: O(n^2), на отсортированном массиве O(n) благодаря флагу swapped
# Память: O(1), устойчивая


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):          # последние i элементов уже на своих местах
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:                     # за проход не было обменов — массив отсортирован
            break


def bubble_sort_verbose(a):
    """То же самое, но печатает массив после каждого прохода."""
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        print(f"проход {i + 1}: {a}")
        if not swapped:
            break


def count_swaps(a):
    """Число обменов пузырька = число инверсий в массиве."""
    a = a[:]
    swaps = 0
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps


if __name__ == "__main__":
    a = [5, 2, 9, 1, 5, 6]
    bubble_sort(a)
    print(a)                            # [1, 2, 5, 5, 6, 9]

    bubble_sort_verbose([5, 2, 9, 1])
    # проход 1: [2, 5, 1, 9]   ← 9 «всплыла» в конец
    # проход 2: [2, 1, 5, 9]
    # проход 3: [1, 2, 5, 9]

    print(count_swaps([4, 3, 2, 1]))    # 6
