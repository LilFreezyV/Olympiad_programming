# Дек (Deque — двусторонняя очередь)

## Оглавление

- [1. Что такое дек](#1-что-такое-дек)
- [2. Операции](#2-операции)
  - [2.1. Про названия `shift` / `unshift`](#21-про-названия-shift--unshift)
- [3. Дек на двусвязном списке](#3-дек-на-двусвязном-списке)
  - [3.1. Длина: считать или хранить](#31-длина-считать-или-хранить)
- [4. Дек на кольцевом буфере](#4-дек-на-кольцевом-буфере)
  - [4.1. Как понять, что буфер заполнен](#41-как-понять-что-буфер-заполнен)
  - [4.2. Список vs кольцевой буфер](#42-список-vs-кольцевой-буфер)
- [5. `collections.deque` в Python](#5-collectionsdeque-в-python)
- [6. Типичные задачи на дек](#6-типичные-задачи-на-дек)
  - [6.1. Максимум в скользящем окне](#61-максимум-в-скользящем-окне)
  - [6.2. BFS 0-1](#62-bfs-0-1)
  - [6.3. Проверка на палиндром](#63-проверка-на-палиндром)
  - [6.4. Длина списка с циклом](#64-длина-списка-с-циклом)
- [7. Частые ошибки](#7-частые-ошибки)
- [8. Шпаргалка](#8-шпаргалка)
- [9. Вопросы для самопроверки](#9-вопросы-для-самопроверки)

---

## 1. Что такое дек

**Дек** (deque, *double-ended queue*, читается «дэк») — структура, в которой добавлять и удалять элементы можно **с обоих концов** за O(1).

```
           push_front                    push_back
               ↓                             ↓
  pop_front ← [ 7 | 3 | 9 | 1 | 4 ] → pop_back
```

Дек объединяет стек и очередь:

- если работать только с одним концом — это **стек**;
- если добавлять в один конец, а забирать из другого — это **очередь**.

> **Аналогия.** Дек — как колода карт, из которой разрешено брать и в которую разрешено класть карты и сверху, и снизу, но не из середины.

---

## 2. Операции

| Операция | Смысл | Сложность |
|---|---|---|
| `push_front(x)` | добавить в начало | O(1) |
| `push_back(x)` | добавить в конец | O(1) |
| `pop_front()` | достать из начала | O(1) |
| `pop_back()` | достать с конца | O(1) |
| `front()`, `back()` | посмотреть крайние элементы | O(1) |
| `len`, пустота | размер | O(1) |

### 2.1. Про названия `shift` / `unshift`

В коде с занятия добавление в начало названо `shift`, а удаление из начала — `unshift`. Имейте в виду: в JavaScript, откуда пришли эти слова, всё **наоборот** — `unshift` добавляет в начало, а `shift` удаляет из начала. В Python (`collections.deque`) эти операции называются `appendleft` и `popleft`. В конспекте используются нейтральные `push_front` / `pop_front`.

---

## 3. Дек на двусвязном списке

Код с занятия — `code/deque_bin_linked_list.py`. В односвязном списке удалить **последний** узел за O(1) нельзя: чтобы сдвинуть `tail`, нужно знать предыдущий узел, а ссылки назад нет. Поэтому для дека нужен **двусвязный** список: у каждого узла есть и `next`, и `prev`.

```
head                                  tail
 ↓                                     ↓
[None | 7 | •]⇄[• | 3 | •]⇄[• | 9 | None]
```

Полная реализация всех четырёх операций:

```python
class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, x):
        node = Node(x)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        else:                      # дек был пуст — новый узел и голова, и хвост
            self.tail = node
        self.head = node
        self.size += 1

    def push_back(self, x):
        node = Node(x)
        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("deque is empty")
        node = self.head
        self.head = node.next
        if self.head is not None:
            self.head.prev = None
        else:                      # забрали последний — хвост тоже пуст
            self.tail = None
        self.size -= 1
        return node.x

    def pop_back(self):
        if self.tail is None:
            raise IndexError("deque is empty")
        node = self.tail
        self.tail = node.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return node.x

    def __len__(self):
        return self.size


d = Deque()
d.push_back(2)
d.push_back(3)
d.push_front(1)                 # 1 2 3
print(d.pop_back())             # 3
print(d.pop_front())            # 1
print(len(d))                   # 1
```

`push_front` / `pop_front` и `push_back` / `pop_back` — **зеркальные** копии друг друга: везде `head ↔ tail` и `next ↔ prev`.

### 3.1. Длина: считать или хранить

В коде с занятия длина считается проходом по списку:

```python
    def length(self):
        node = self.head
        answer = 0
        while node is not None:
            node = node.next
            answer += 1
        return answer
```

Это O(n). Если хранить счётчик `size` и менять его в каждой операции (как выше), длина будет O(1).

Обратите внимание: в проходе используется отдельная переменная `node`, а `self.head` не меняется. Если бы цикл двигал сам `self.head`, после подсчёта длины дек оказался бы «пустым» — ссылка на начало потерялась бы.

---

## 4. Дек на кольцевом буфере

Код с занятия — `code/deque.py`. Вместо узлов используется **обычный массив**, который мысленно свёрнут в кольцо: после последней ячейки идёт снова нулевая. Храним индекс начала `start` и количество элементов `size`.

```
N = 8, start = 6, size = 4

индекс:   0   1   2   3   4   5   6   7
         [ c | d |   |   |   |   | a | b ]
                                   ↑
                                 start
логический порядок: a b c d
```

- Элемент с логическим номером `i` лежит в ячейке `(start + i) % N`.
- `push_front`: `start = (start - 1) % N`, пишем в `a[start]`.
- `push_back`: пишем в `a[(start + size) % N]`.
- Когда `size == N`, массив заполнен — создаём новый в **2 раза больше** и переписываем элементы по порядку, начиная с индекса 0 (как в динамическом массиве).

```python
class RingDeque:
    def __init__(self, capacity=4):
        self.a = [None] * capacity
        self.start = 0
        self.size = 0

    def _grow(self):
        n = len(self.a)
        new_a = [None] * (2 * n)
        for i in range(self.size):
            new_a[i] = self.a[(self.start + i) % n]   # раскладываем по порядку
        self.a = new_a
        self.start = 0

    def push_front(self, x):
        if self.size == len(self.a):
            self._grow()
        self.start = (self.start - 1) % len(self.a)
        self.a[self.start] = x
        self.size += 1

    def push_back(self, x):
        if self.size == len(self.a):
            self._grow()
        self.a[(self.start + self.size) % len(self.a)] = x
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise IndexError("deque is empty")
        x = self.a[self.start]
        self.a[self.start] = None
        self.start = (self.start + 1) % len(self.a)
        self.size -= 1
        return x

    def pop_back(self):
        if self.size == 0:
            raise IndexError("deque is empty")
        i = (self.start + self.size - 1) % len(self.a)
        x = self.a[i]
        self.a[i] = None
        self.size -= 1
        return x

    def __getitem__(self, i):          # доступ по индексу за O(1)!
        return self.a[(self.start + i) % len(self.a)]

    def __len__(self):
        return self.size


d = RingDeque(2)
for x in [3, 4, 5]:
    d.push_back(x)
d.push_front(2)
d.push_front(1)                   # 1 2 3 4 5, массив уже расширялся
print([d[i] for i in range(len(d))])   # [1, 2, 3, 4, 5]
print(d.pop_front(), d.pop_back())      # 1 5
```

### 4.1. Как понять, что буфер заполнен

Это главная тонкость кольцевого буфера. Если хранить только два указателя `start` и `finish`, то и у пустого, и у полного буфера они **совпадают** — отличить нельзя. Варианты решения:

1. **Хранить `size`** (как выше) — самый простой и надёжный.
2. Всегда оставлять **одну ячейку пустой**: буфер полон, когда `(finish + 1) % N == start`.
3. Проверять, **занята ли ячейка**, куда собираемся писать (`a[start - 1] is not None`) — так сделано в коде с занятия. Работает, только если в дек никогда не кладут `None`, и требует аккуратно поддерживать оба указателя при каждой операции.

### 4.2. Список vs кольцевой буфер

| | Двусвязный список | Кольцевой буфер |
|---|---|---|
| Операции с концами | O(1) | O(1) амортизированно |
| Доступ к `i`-му элементу | O(n) | **O(1)** |
| Память | узел на каждый элемент (+2 ссылки) | один массив, иногда с запасом |
| Сложность кода | проще | нужно аккуратно с `% N` и расширением |

`collections.deque` в Python — гибрид: двусвязный список **блоков** по 64 элемента.

---

## 5. `collections.deque` в Python

На олимпиаде свой дек писать не нужно — есть встроенный:

```python
from collections import deque

d = deque([2, 3])
d.append(4)            # в конец        → deque([2, 3, 4])
d.appendleft(1)        # в начало       → deque([1, 2, 3, 4])
d.pop()                # с конца        → 4
d.popleft()            # из начала      → 1
d[0], d[-1]            # крайние        → (2, 3)
len(d)                 # 2

d = deque([1, 2, 3, 4, 5])
d.rotate(2)            # сдвиг вправо   → deque([4, 5, 1, 2, 3])
d.rotate(-2)           # сдвиг влево    → deque([1, 2, 3, 4, 5])

d = deque(maxlen=3)    # дек ограниченного размера
for x in range(5):
    d.append(x)        # старые элементы вытесняются с другого конца
print(d)               # deque([2, 3, 4], maxlen=3)
```

Осторожно: `d[i]` для элементов **из середины** — O(n), а не O(1), как у списка. Дек хорош для концов, а не для произвольного доступа.

---

## 6. Типичные задачи на дек

### 6.1. Максимум в скользящем окне

Дан массив и число `k`. Для каждого окна `a[i : i + k]` найти максимум. Наивно — O(n·k), с деком — **O(n)**.

Идея: в деке храним **индексы** элементов текущего окна, причём их значения идут **по убыванию**. Тогда максимум окна всегда в начале дека.

- Новый элемент выталкивает с **конца** все меньшие или равные — они уже никогда не станут максимумом (новый элемент больше и проживёт в окне дольше).
- Если индекс в **начале** вышел за левую границу окна — выкидываем его.

```python
from collections import deque

def sliding_max(a, k):
    d = deque()                          # индексы, значения по убыванию
    result = []
    for i, x in enumerate(a):
        while d and a[d[-1]] <= x:
            d.pop()
        d.append(i)
        if d[0] <= i - k:                # вышел из окна слева
            d.popleft()
        if i >= k - 1:
            result.append(a[d[0]])
    return result


print(sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
```

Каждый индекс добавляется и удаляется из дека не больше одного раза → O(n). Это **монотонный дек** — родственник монотонного стека из темы «Стек и очередь».

### 6.2. BFS 0-1

Кратчайший путь в графе, где рёбра имеют вес **0 или 1**. Вершину, до которой дошли по ребру веса 0, кладём в **начало** дека, по ребру веса 1 — в **конец**. Получается O(V + E) вместо Дейкстры за O(E log V).

```python
from collections import deque

def bfs01(graph, start, n):
    INF = float("inf")
    dist = [INF] * n
    dist[start] = 0
    d = deque([start])
    while d:
        v = d.popleft()
        for u, w in graph[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                if w == 0:
                    d.appendleft(u)
                else:
                    d.append(u)
    return dist


graph = [[(1, 1), (2, 0)], [(3, 0)], [(1, 0), (3, 1)], []]
print(bfs01(graph, 0, 4))   # [0, 0, 0, 0]
```

### 6.3. Проверка на палиндром

Снимаем по символу с обоих концов и сравниваем:

```python
from collections import deque

def is_palindrome(s):
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


print(is_palindrome("level"))   # True
print(is_palindrome("hello"))   # False
```

(Конечно, на Python проще `s == s[::-1]`, но задача хорошо показывает смысл дека.)

### 6.4. Длина списка с циклом

Задача из `code/task.py`: дан узел, начиная с которого ссылки `next` рано или поздно замыкаются в кольцо. Нужно найти количество **различных** узлов.

В первой версии решения посещённые узлы хранились в **списке**, а проверка `head not in pointers` по списку — это O(n) на каждом шаге, итого **O(n²)**. Сейчас в `code/task.py` используется **множество**: проверка стала O(1), и всё решение — O(n). То же самое в компактной записи:

```python
def length(head):
    seen = set()
    node = head
    while node is not None and node not in seen:
        seen.add(node)
        node = node.next
    return len(seen)
```

Можно обойтись и вовсе без дополнительной памяти — алгоритмом Флойда «черепаха и заяц» (см. конспект `themes/linked_list/theory/theory.md`, раздел 6.2).

---

## 7. Частые ошибки

1. **Не обновить второй конец при опустошении.** Удалили последний элемент через `pop_front` — нужно обнулить и `tail`; через `pop_back` — и `head`.
2. **Забыть одну из ссылок в двусвязном списке.** При вставке в начало нужны **обе**: `node.next = head` и `head.prev = node`. Если забыть `prev`, `pop_back` потом «сломается».
3. **Двигать `self.head` при обходе** (например, при подсчёте длины) — дек теряет начало.
4. **Путаница «полон / пуст» в кольцевом буфере**, когда хранятся только два указателя (раздел 4.1).
5. **Отрицательный индекс в кольце.** В Python `(start - 1) % N` корректно даёт `N - 1` при `start = 0`, а в C++/Java — нет (там `-1 % N == -1`). Пишите `(start - 1 + N) % N`, если переносите код.
6. **`d[i]` из середины `collections.deque`** — O(n). Для произвольного доступа нужен список.
7. **`x in d`** или `x in list` внутри цикла — O(n) на проверку. Для «видели ли уже» используйте `set`.

---

## 8. Шпаргалка

```python
from collections import deque

d = deque()                  # или deque(iterable), deque(maxlen=k)
d.append(x)                  # в конец           O(1)
d.appendleft(x)              # в начало          O(1)
d.pop()                      # с конца           O(1)
d.popleft()                  # из начала         O(1)
d[0], d[-1]                  # крайние           O(1)
d.rotate(k)                  # сдвиг по кругу    O(k)
len(d), not d                # размер, пустота

# монотонный дек: max/min в скользящем окне за O(n)
# 0-1 BFS: вес 0 → appendleft, вес 1 → append
# кольцевой буфер: индекс (start + i) % N, храните size
```

---

## 9. Вопросы для самопроверки

1. В пустой дек выполнили: `push_back(1)`, `push_front(2)`, `push_back(3)`, `push_front(4)`, `pop_back()`, `pop_front()`. Что в нём осталось?
2. Почему для дека на связном списке нужен именно **двусвязный** список?
3. Кольцевой буфер на 8 ячеек, `start = 6`, `size = 4`. В какую ячейку попадёт элемент при `push_back`? А при `push_front`?
4. Почему в алгоритме «максимум в скользящем окне» можно выбросить из дека меньшие элементы и не бояться, что они потом понадобятся?
5. Какая была бы сложность решения из `code/task.py`, если хранить посещённые узлы в списке, а не в множестве?

<details>
<summary>Ответы</summary>

1. **`[2, 1]`.** После вставок: `4 2 1 3`. `pop_back` убирает 3, `pop_front` — 4.
2. Чтобы удалить последний элемент за O(1), нужно сдвинуть `tail` на предыдущий узел, а ссылка на предыдущий есть только в двусвязном списке.
3. `push_back` → ячейка `(6 + 4) % 8 = 2`. `push_front` → `start` станет `(6 - 1) % 8 = 5`, элемент попадёт в ячейку 5.
4. Выброшенный элемент меньше (или равен) нового, а новый стоит **правее** и, значит, останется в окне дольше. Пока выброшенный был бы в окне, в окне есть и новый, который больше, — выброшенный никогда не стал бы максимумом.
5. **O(n²)**: проверка `x in list` занимает O(n) и выполняется на каждом шаге. С `set` получается O(n); алгоритм Флойда даёт O(n) и O(1) памяти.

</details>
