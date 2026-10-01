class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_pivot(head, cycle_length):
    if head is None or cycle_length <= 0:
        return None
    l = head
    r = head

    for _ in range(cycle_length):
        r = r.next

    while l is not r:
        l = l.next
        r = r.next

    return l


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

pivot = find_pivot(n1, cycle_length=4)
print(pivot.value)  # 3
