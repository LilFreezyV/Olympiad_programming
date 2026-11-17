from BST import *


def find_sum(head, a, b):
    nodeA, levelA = find_i(head, a)
    nodeB, levelB = find_i(head, b)
    diff = max(levelA, levelB)
    s = 0
    if levelA - levelB > 0:
        s += count(nodeA.right)
        for i in range(levelA - levelB):
            if i != 0:
                s += nodeA.x
            nodeA = nodeA.parent


    if levelA - levelB < 0:
        s += count(nodeA.right)
        for i in range(levelB - levelA):
            if i != 0:
                s += nodeA.x
            nodeA = nodeA.parent






def find_i_req(i, head):
    if head is None or i < 0 or i > count(head):
        return None
    left_count = count(head.left)
    if i < left_count:
        return find_i_req(i, head.left)
    if i == left_count:
        return head
    return find_i_req(i - left_count - 1, head.right)




def find_i(head, i):
    value = None
    c = 0
    k = 0
    while head.x != i:
        c += 1
        if count(head.left) + k >= i:
            head = head.left
        else:
            k += count(head.left) + 1
            head = head.right
    return head, c