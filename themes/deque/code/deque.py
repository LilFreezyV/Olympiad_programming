class Deque():
    def __init__(self, N):
        self.start = 0
        self.finish = 0
        self.N = N
        self.array = [None] * N

    def shift(self, x):
        if self.array[self.start - 1] is not None:
            self.N *= 2
            new_arr = [None] * self.N
            new_arr[:self.N // 2 - self.start] = self.array[self.start:]
            new_arr[self.N // 2 - self.start:self.N // 2] = self.array[:self.finish]
            self.array = new_arr
            self.start = 0
            self.finish = self.N // 2
        self.array[self.start - 1] = x
        self.start = (self.N + self.start - 1) % self.N

    def unshift(self):
        if self.array[self.start] is None:
            raise IndexError("deque is empty")
        r = self.array[self.start]
        self.array[self.start] = None
        self.start = (self.start + 1) % self.N
        return r;

    def show(self):
        print(self.start)
        print(self.finish)


"""__init__ создаёт пустой «стол» из None, а оба указателя ставит на 0.

shift(x) задуман как «посадить x перед первым», то есть добавить в начало. Сначала он проверяет стул слева от start. Если там кто-то сидит, значит стол полный: голова упёрлась в хвост. Тогда стол удваивается, и всех пересаживают на новый стол по порядку. Сначала идут те, кто сидел от start до конца старого массива, потом те, кто сидел от 0 до finish. После этого очередь начинается с 0-го стула, а освободившееся место в конце нового массива (стул -1) достаётся x. Указатель start сдвигается на него.

unshift() забирает первого: запоминает array[start], ставит на его место None, сдвигает start на один вправо по кругу и возвращает запомненное. Это аналог popleft."""

d = Deque(20)
d.shift(1)
d.shift(2)
d.shift(3)
d.show()
