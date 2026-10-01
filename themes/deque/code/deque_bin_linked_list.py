class Node():
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Deque():
    def __init__(self):
        self.head = None
        self.tail = None

    def shift(self, x):
        r = Node(x)
        r.next = self.head
        if self.head is not None:
            self.head.prev = r
        else:
            self.tail = r
        self.head = r

    def unshift(self):
        if self.head is None:
            raise IndexError("deque is empty")
        el = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return el.x

    # def length(self):
    #     answer = 1
    #     start_head = self.head.next
    #     while start_head != head:
    #         head = head.next
    #         answer += 1
    #     return answer

    def length(self):
        head = self.head
        answer = 0
        while head is not None:
            head = head.next
            answer += 1
        return answer  # --> возвращает длину массива

    # def length(self):
    #     answer = 0
    #     while self.head != None:
    #         next_head = self.head.next
    #         self.head.next = None
    #         self.head = next_head
    #         answer += 1
    #     return answer


deque = Deque()
deque.shift(1)
deque.shift(1)
deque.shift(1)
deque.shift(1)
deque.shift(1)
print(deque.length())
