"""Неявный Treap: последовательность с range reverse и range sum.

Все диапазоны полуоткрытые [l, r), индексация с нуля.
"""
import random


class Node:
    __slots__ = ("value", "priority", "left", "right", "size", "total", "reversed")

    def __init__(self, value):
        self.value = value
        self.priority = random.getrandbits(64)
        self.left = self.right = None
        self.size = 1
        self.total = value
        self.reversed = False


def size(t):
    return t.size if t else 0


def total(t):
    return t.total if t else 0


def update(t):
    if t:
        t.size = 1 + size(t.left) + size(t.right)
        t.total = t.value + total(t.left) + total(t.right)


def push(t):
    """Протолкнуть отложенный разворот детям."""
    if t and t.reversed:
        t.left, t.right = t.right, t.left
        if t.left:
            t.left.reversed ^= True
        if t.right:
            t.right.reversed ^= True
        t.reversed = False


def split(t, count):
    """Первые count элементов и остаток."""
    if t is None:
        return None, None
    push(t)
    if size(t.left) >= count:
        left, t.left = split(t.left, count)
        update(t)
        return left, t
    t.right, right = split(t.right, count - size(t.left) - 1)
    update(t)
    return t, right


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    push(left)
    push(right)
    if left.priority > right.priority:
        left.right = merge(left.right, right)
        update(left)
        return left
    right.left = merge(left, right.left)
    update(right)
    return right


def build(values):
    root = None
    for value in values:
        root = merge(root, Node(value))
    return root


def reverse_range(root, left, right):
    """Развернуть элементы на позициях [left, right)."""
    a, tail = split(root, left)
    middle, c = split(tail, right - left)
    if middle:
        middle.reversed ^= True
    return merge(a, merge(middle, c))


def range_sum(root, left, right):
    """Сумма элементов [left, right); исходное дерево восстанавливается."""
    a, tail = split(root, left)
    middle, c = split(tail, right - left)
    answer = total(middle)
    root = merge(a, merge(middle, c))
    return answer, root


def to_list(t):
    if t is None:
        return []
    push(t)
    return to_list(t.left) + [t.value] + to_list(t.right)


if __name__ == "__main__":
    root = build([10, 20, 30, 40, 50, 60])
    root = reverse_range(root, 1, 5)
    print(to_list(root))          # [10, 50, 40, 30, 20, 60]
    answer, root = range_sum(root, 1, 4)
    print(answer)                 # 120
    print(to_list(root))          # последовательность не изменилась
