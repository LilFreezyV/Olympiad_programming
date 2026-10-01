class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_pivot(head):
    c_length = cycle_length(head)
    if head is None or c_length <= 0:
        return None
    l = head
    r = head

    for _ in range(c_length):
        r = r.next

    while l is not r:
        l = l.next
        r = r.next

    return l


def cycle_length(head):
    if head is None:
        return 0

    slow = head
    fast = head

    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return 0

    length = 1
    cur = slow.next
    while cur is not slow:
        cur = cur.next
        length += 1
    return length


# создаём узлы
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n3  # замыкаем цикл на n3

pivot = find_pivot(n1)
length = cycle_length(n1)
print(length)  # 3
