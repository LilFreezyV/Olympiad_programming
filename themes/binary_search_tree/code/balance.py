from math import log2
from BST import *


def balance(head, n):
    for layer in range(1, log2(n) + 1):
        for i in range(2 ** layer):
            cur = find(head, n * (2 * i + 1) / 2 ** (layer + 1))
            parent = find(head, n *  (i + 1) / (2 ** layer))
            if i % 2 == 0:
                parent.left.parent = None
            else:
                parent.right.parent = None
            up(cur)
            cur.parent = parent
            if i % 2 == 0:
                parent.left = cur
            else:
                parent.right = cur

