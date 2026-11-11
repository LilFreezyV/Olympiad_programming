"""Декартово дерево по ключу: множество с rank/kth и суммой на отрезке."""
import random


class Node:
    __slots__ = ("key", "priority", "left", "right", "size", "total")

    def __init__(self, key, priority=None):
        self.key = key
        self.priority = random.getrandbits(64) if priority is None else priority
        self.left = self.right = None
        self.size = 1
        self.total = key


def size(t):
    return t.size if t else 0


def total(t):
    return t.total if t else 0


def update(t):
    if t:
        t.size = 1 + size(t.left) + size(t.right)
        t.total = t.key + total(t.left) + total(t.right)


def split(t, key):
    """Разделить на ключи < key и >= key."""
    if t is None:
        return None, None
    if t.key < key:
        t.right, right = split(t.right, key)
        update(t)
        return t, right
    left, t.left = split(t.left, key)
    update(t)
    return left, t


def merge(left, right):
    """Объединить деревья, если все ключи left < всех ключей right."""
    if left is None:
        return right
    if right is None:
        return left
    if left.priority > right.priority:  # max-heap по приоритету
        left.right = merge(left.right, right)
        update(left)
        return left
    right.left = merge(left, right.left)
    update(right)
    return right


def contains(t, key):
    while t:
        if key == t.key:
            return True
        t = t.left if key < t.key else t.right
    return False


def insert(t, key):
    if contains(t, key):  # здесь храним множество без дубликатов
        return t
    left, right = split(t, key)
    return merge(merge(left, Node(key)), right)


def erase(t, key):
    """Удалить ключ, если он присутствует."""
    if t is None:
        return None
    if key == t.key:
        return merge(t.left, t.right)
    if key < t.key:
        t.left = erase(t.left, key)
    else:
        t.right = erase(t.right, key)
    update(t)
    return t


def kth(t, k):
    """k-й ключ по возрастанию, индексация с нуля."""
    if not 0 <= k < size(t):
        raise IndexError("k is out of range")
    left_size = size(t.left)
    if k < left_size:
        return kth(t.left, k)
    if k == left_size:
        return t.key
    return kth(t.right, k - left_size - 1)


def rank(t, key):
    """Количество ключей, строго меньших key."""
    result = 0
    while t:
        if key <= t.key:
            t = t.left
        else:
            result += 1 + size(t.left)
            t = t.right
    return result


def range_sum(t, lo, hi):
    """Сумма ключей lo <= key <= hi за O(h), не меняя дерево."""
    if t is None:
        return 0
    if t.key < lo:
        return range_sum(t.right, lo, hi)
    if t.key > hi:
        return range_sum(t.left, lo, hi)
    return t.key + range_sum(t.left, lo, hi) + range_sum(t.right, lo, hi)


def inorder(t):
    return inorder(t.left) + [t.key] + inorder(t.right) if t else []


if __name__ == "__main__":
    root = None
    for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        root = insert(root, x)

    print(inorder(root))          # [1, 3, 4, 6, 7, 8, 10, 13, 14]
    print(kth(root, 3))            # 6
    print(rank(root, 8))           # 5
    print(range_sum(root, 4, 10))  # 35

    root = erase(root, 8)
    print(inorder(root))          # [1, 3, 4, 6, 7, 10, 13, 14]
