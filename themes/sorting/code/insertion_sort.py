# Сортировка вставками (Insertion sort)
# Время: O(n^2), на почти отсортированном массиве почти O(n)
# Память: O(1), устойчивая


def insertion_sort(a):
    for i in range(1, len(a)):
        x = a[i]                            # «карта», которую вставляем
        j = i - 1
        while j >= 0 and a[j] > x:          # строго >, чтобы не переставлять равные
            a[j + 1] = a[j]                 # сдвигаем больший элемент вправо
            j -= 1
        a[j + 1] = x


def insertion_sort_verbose(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
        print(f"вставили {x}: {a[:i + 1]} | {a[i + 1:]}")


if __name__ == "__main__":
    a = [12, 11, 13, 5, 6]
    insertion_sort(a)
    print(a)                                # [5, 6, 11, 12, 13]

    insertion_sort_verbose([2, 5, 9, 1, 6])
    # вставили 5: [2, 5] | [9, 1, 6]
    # вставили 9: [2, 5, 9] | [1, 6]
    # вставили 1: [1, 2, 5, 9] | [6]
    # вставили 6: [1, 2, 5, 6, 9] | []
