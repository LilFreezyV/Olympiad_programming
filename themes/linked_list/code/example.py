class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Добавление в начало
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Добавление в конец
    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Удаление по значению
    def delete(self, key):
        current = self.head
        prev = None
        while current:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    # Вывод списка
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")