# Встроенная сортировка Python: sorted() и list.sort()
# Алгоритм Timsort (слияние + вставки), O(n log n), устойчивая
# На олимпиадах почти всегда используют именно её
from functools import cmp_to_key

# --- sorted и sort ---
a = [5, 2, 9, 1]
b = sorted(a)                   # новый список, a не меняется
a.sort()                        # на месте, возвращает None
print(a, b)                     # [1, 2, 5, 9] [1, 2, 5, 9]

# --- обратный порядок и ключ ---
nums = [5, -2, 9, -10]
print(sorted(nums, reverse=True))           # [9, 5, -2, -10]
print(sorted(nums, key=abs))                # [-2, 5, 9, -10]

words = ["banana", "Apple", "cherry", "kiwi"]
print(sorted(words))                        # ['Apple', 'banana', 'cherry', 'kiwi']
print(sorted(words, key=str.lower))         # без учёта регистра
print(sorted(words, key=len))               # ['kiwi', 'Apple', 'banana', 'cherry']

# --- несколько ключей: оценка по убыванию, при равенстве имя по возрастанию ---
pupils = [("Вика", 5), ("Аня", 5), ("Боря", 4)]
print(sorted(pupils, key=lambda p: (-p[1], p[0])))
# [('Аня', 5), ('Вика', 5), ('Боря', 4)]

# --- то же через устойчивость: сначала второстепенный ключ, потом главный ---
pupils.sort(key=lambda p: p[0])
pupils.sort(key=lambda p: p[1], reverse=True)
print(pupils)                               # [('Аня', 5), ('Вика', 5), ('Боря', 4)]


# --- свой компаратор: составить из чисел наибольшее число ---
def cmp(x, y):
    if x + y > y + x:
        return -1                           # x раньше y
    if x + y < y + x:
        return 1                            # y раньше x
    return 0


print("".join(sorted(map(str, [3, 30, 34, 5, 9]), key=cmp_to_key(cmp))))   # 9534330

# --- индексы в порядке сортировки (argsort) ---
a = [30, 10, 20]
print(sorted(range(len(a)), key=lambda i: a[i]))    # [1, 2, 0]

# --- ловушка: строки вместо чисел ---
s = "10 9 2"
print(sorted(s.split()))                    # ['10', '2', '9'] — сравниваются строки!
print(sorted(map(int, s.split())))          # [2, 9, 10]
