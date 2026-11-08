class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


def add(where, x):
    if x < where.x:
        if not where.left:
            where.left = Node(x)
        else:
            add(where.left, x)
    else:
        if not where.right:
            where.right = Node(x)
        else:
            add(where.right, x)


def find(x, node):
    if node is None:
        return False
    if x == node.x:
        return True
    if x < node.x:
        return find(x, node.left)
    else:
        return find(x, node.right)
