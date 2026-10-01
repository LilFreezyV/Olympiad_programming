class MyStack():
    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)

    def pop(self):
        r = self.a[-1]
        self.a.pop()
        return r


# z = MyStack()
# z.push(2)
# z.push(3)
# print(z.pop())

class My2Class():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.p = None

    def add_next(self, p):
        self.p = p


# z = My2Class()
# z.p = 4 # одно и то же
# z.add_next(4) # одно и то же
# z2 = My2Class()
# z2.p = z
# z2.p.x = 3

class MyClass():
    def __init__(self, x):
        self.x = x
        self.p = None


# z = MyClass(4)
# z2 = MyClass(3)
# z3 = MyClass(2)
# z4 = MyClass(1)
# z.p = z2
# z2.p = z3
# z3.p = z4
# print(z.p.p.p.x)
# print(z.p.p.x)
# print(z.p.x)
# print(z.x)

z = MyClass(0)
h = z
for i in range(100):
    k = MyClass(i + 1)
    z.p = k
    z = k

u = h
while u != None:
    print(u.x)
    u = u.p

def add(x):
    z.p = MyClass(x)
    k = z.p

