class myClass():
    def __init__(self):
        self.x = 0
        self.y = 0

    def add(self):
        self.x = self.x + 1


z = myClass()
z.x = 2
z.x = z.y + 4
z.add()
print(z.x)
