class Node():
    def __init__(self, x):
        self.x = x
        self.next = None


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        if not self.tail:
            new_node = Node(x)
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = Node(x)
            self.tail.next.x = x
            self.tail = self.tail.next

    def pop(self):
        r = self.head.x
        self.head = self.head.next
        if self.head is None:   # забрали последний элемент — хвост тоже должен стать None
            self.tail = None
        return r

    def get(self, i):
        r = self.head
        for _ in range(i):
            r = r.next
        return r.x

    def _del(self, i):
        if i == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            r = self.head
            for _ in range(i - 1):
                r = r.next
            if r.next == self.tail:
                self.tail = r
            r.next = r.next.next    # удаляем узел всегда, а не только когда он хвост





z = Queue()
z.add(1)
z.add(2)
z.add(3)
z.add(4)
z.add(5)
z.add(6)
print(z.get(5))

# print(z.get(2))
# print(z.get(4))
z._del(5)
print(z.get(4))
