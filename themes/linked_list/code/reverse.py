class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    if head is None or head.next is None:
        return head

    prev = None
    _next = head.next
    cur = head
    while cur != None:
        cur.next = prev
        prev = cur
        cur = _next
        if _next:
            _next = _next.next
    head = prev

    return head


def to_list(head):
    """Превращает список в массив для сравнения."""
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


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
# пустой список

print(to_list(n1))
result = reverse(n1)
print("список:", to_list(result))
