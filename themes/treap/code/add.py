"""Вставка узла в Treap через split и merge.

Узел имеет поля x (ключ), y (приоритет), left и right.
split делит на ключи <= k и > k; merge требует, чтобы все ключи
первого дерева были меньше ключей второго.
"""


def split(a, k):
    if a is None:
        return None, None
    if a.x > k:
        left, a.left = split(a.left, k)
        return left, a
    else:
        a.right, right = split(a.right, k)
        return a, right


def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.y > b.y:
        a.right = merge(a.right, b)
        return a
    else:
        b.left = merge(a, b.left)
        return b


def add(root, node):
    """Вставить node; предполагается, что такого ключа в дереве нет."""
    left, right = split(root, node.x)
    return merge(merge(left, node), right)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None


def show(root, indent="", side="root"):
    if root is None:
        return
    print(f"{indent}{side}: ({root.x}, {root.y})")
    show(root.left, indent + "  ", "L")
    show(root.right, indent + "  ", "R")


if __name__ == "__main__":
    root = Node(8, 95)
    root.left = Node(3, 72)
    root.left.left = Node(1, 40)
    root.left.right = Node(6, 58)
    root.right = Node(12, 81)
    root.right.left = Node(10, 33)

    root = add(root, Node(9, 88))
    show(root)
