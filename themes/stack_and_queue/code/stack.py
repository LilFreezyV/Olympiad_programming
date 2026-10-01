class Node():
    def __init__(self, x):
        self.x = x
        self.next = None


class Stack():
    def __init__(self):
        self.head = None

    def add(self, x):
        newNode = Node(x)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        r = self.head.x
        self.head = self.head.next
        return r



z = Stack()
z.add(1)
z.add(2)
z.pop()
z.pop()

# # после add(1):
# head ──► [ x=1 | next=None ]
#
# # после add(2):
# # сначала: head.next = Node(2)
# head ──► [ x=1 | next ] ──► [ x=2 | next=None ]
# # затем: head = Node(2)
#                          ┌── head
#                          ▼
#         [ x=1 | next ] ──► [ x=2 | next=None ]