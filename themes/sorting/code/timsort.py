# Timsort (упрощённая версия) — так устроены sorted() и list.sort() в Python
# 1. Ищем в массиве готовые упорядоченные куски — «пробеги» (runs).
#    Строго убывающий пробег разворачиваем.
# 2. Короткие пробеги дополняем до длины minrun бинарными вставками.
# 3. Пробеги кладём в стек и сливаем так, чтобы сливались куски похожей длины.
# Время: O(n) на почти отсортированных данных, O(n log n) в худшем случае
# Память: O(n), устойчивая
# В настоящем Timsort есть ещё «галоп» (galloping) при слиянии — здесь его нет.
import random
import time
from functools import total_ordering

MIN_MERGE = 32


def calc_minrun(n):
    """Для n >= 32 — число от 16 до 32, такое что n / minrun — степень двойки или чуть меньше.
    Тогда пробеги потом сливаются почти поровну. (В CPython порог 64 и minrun от 32 до 64.)"""
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def count_run(a, lo, n):
    """Находит пробег, начинающийся в lo. Возвращает его конец (не включительно)."""
    hi = lo + 1
    if hi == n:
        return hi
    if a[hi] < a[lo]:                           # строго убывающий пробег
        while hi < n and a[hi] < a[hi - 1]:
            hi += 1
        a[lo:hi] = a[lo:hi][::-1]               # разворачиваем (строго — чтобы не нарушить устойчивость)
    else:                                       # неубывающий пробег
        while hi < n and a[hi] >= a[hi - 1]:
            hi += 1
    return hi


def binary_insertion_sort(a, lo, hi, start):
    """a[lo:start] уже отсортирован; вставляем в него a[start:hi], место ищем бинпоиском."""
    for i in range(start, hi):
        x = a[i]
        left, right = lo, i
        while left < right:                     # ищем первый элемент > x (bisect_right)
            mid = (left + right) // 2
            if x < a[mid]:
                right = mid
            else:
                left = mid + 1
        a[left + 1:i + 1] = a[left:i]           # сдвигаем кусок вправо одним срезом
        a[left] = x


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


def merge_at(a, runs, i):
    """Сливает пробеги runs[i] и runs[i + 1] (они соседние в массиве)."""
    start1, len1 = runs[i]
    start2, len2 = runs[i + 1]
    a[start1:start2 + len2] = merge(a[start1:start1 + len1], a[start2:start2 + len2])
    runs[i] = (start1, len1 + len2)
    del runs[i + 1]


def merge_collapse(a, runs):
    """Поддерживает правила для трёх верхних пробегов стека (длины A, B, C сверху вниз — C, B, A):
         A > B + C  и  B > C.
    Тогда длины в стеке растут не медленнее чисел Фибоначчи, стек короткий (O(log n)),
    а сливаются куски примерно одинаковой длины — как в обычном merge sort."""
    while len(runs) > 1:
        n = len(runs) - 2
        if (n > 0 and runs[n - 1][1] <= runs[n][1] + runs[n + 1][1]) or \
           (n > 1 and runs[n - 2][1] <= runs[n - 1][1] + runs[n][1]):
            if runs[n - 1][1] < runs[n + 1][1]:
                n -= 1
            merge_at(a, runs, n)
        elif runs[n][1] <= runs[n + 1][1]:
            merge_at(a, runs, n)
        else:
            break


def merge_force_collapse(a, runs):
    """В конце сливаем всё, что осталось в стеке."""
    while len(runs) > 1:
        n = len(runs) - 2
        if n > 0 and runs[n - 1][1] < runs[n + 1][1]:
            n -= 1
        merge_at(a, runs, n)


def timsort(a):
    n = len(a)
    if n < 2:
        return
    minrun = calc_minrun(n)
    runs = []                                   # стек пробегов: (начало, длина)
    lo = 0
    while lo < n:
        hi = count_run(a, lo, n)
        if hi - lo < minrun:                    # короткий пробег — дополняем вставками
            force = min(lo + minrun, n)
            binary_insertion_sort(a, lo, force, hi)
            hi = force
        runs.append((lo, hi - lo))
        merge_collapse(a, runs)
        lo = hi
    merge_force_collapse(a, runs)


def find_runs(a):
    """Только для наглядности: длины естественных пробегов в массиве."""
    a = a[:]
    lengths = []
    lo = 0
    while lo < len(a):
        hi = count_run(a, lo, len(a))
        lengths.append(hi - lo)
        lo = hi
    return lengths


if __name__ == "__main__":
    a = [random.randint(0, 99) for _ in range(100)]
    timsort(a)
    print(a == sorted(a))                               # True

    print(find_runs([1, 2, 5, 9, 8, 4, 3, 6, 7, 7, 0]))  # [4, 3, 3, 1]
    # [1 2 5 9] [8 4 3] [6 7 7] [0] — убывающий [8 4 3] будет развёрнут в [3 4 8]

    print(calc_minrun(64), calc_minrun(65), calc_minrun(1000), calc_minrun(10**6))   # 16 17 32 31

    # Устойчивость: объекты сравниваются ТОЛЬКО по оценке, номер ученика в сравнении не участвует
    @total_ordering
    class Pupil:
        def __init__(self, score, number):
            self.score = score
            self.number = number

        def __eq__(self, other):
            return self.score == other.score

        def __lt__(self, other):
            return self.score < other.score

    pupils = [Pupil(random.randint(2, 5), i) for i in range(200)]
    timsort(pupils)
    # среди равных оценок номера должны остаться в исходном порядке
    print(all(p.number < q.number for p, q in zip(pupils, pupils[1:]) if p.score == q.score))   # True

    # Почти отсортированный массив: Timsort находит несколько длинных пробегов
    n = 100_000
    data = list(range(n))
    for _ in range(10):                                 # немного «портим» порядок
        i, j = random.randrange(n), random.randrange(n)
        data[i], data[j] = data[j], data[i]
    print(f"\nпочти отсортированный массив, n = {n}: пробегов {len(find_runs(data))}")

    for name, arr in [("случайный", [random.randint(0, 10**9) for _ in range(n)]),
                      ("почти отсортированный", data),
                      ("отсортированный по убыванию", list(range(n, 0, -1)))]:
        b = arr[:]
        t = time.perf_counter()
        timsort(b)
        dt = time.perf_counter() - t
        assert b == sorted(arr)
        print(f"  {name:>28}: {dt:.3f} с")
