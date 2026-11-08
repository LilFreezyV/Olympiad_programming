class MyQueue:
    def __init__(self):
        self.in_stack = []    # сюда кладём
        self.out_stack = []   # отсюда забираем

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()                      # гарантируем, что out_stack не пуст
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


# Проверка
q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())    # 1
print(q.peek())   # 2
q.push(4)
print(q.pop())    # 2
print(q.pop())    # 3
print(q.pop())    # 4
print(q.empty())  # True