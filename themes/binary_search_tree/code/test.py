class Node:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


def add(where, x):
    if x < where.x:
        if not where.left:
            where.left = Node(x)
        else:
            add(where.left, x)
    else:
        if not where.right:
            where.right = Node(x)
        else:
            add(where.right, x)


def find(x, node):
    if node is None:
        return False
    if x == node.x:
        return True
    if x < node.x:
        return find(x, node.left)
    else:
        return find(x, node.right)


# --- Проверка работоспособности ---

root = Node(50)

# Добавляем элементы
values = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85, 1000]
for v in values:
    add(root, v)


def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.x)
        inorder(node.right, result)
    return result


# Проверка обхода — должен быть отсортированным
sorted_values = inorder(root)
print("Отсортированный обход:", sorted_values)
assert sorted_values == sorted([50] + values), "Ошибка построения дерева!"

# Проверяем поиск существующих элементов
for v in [50] + values:
    assert find(v, root) is True, f"Элемент {v} не найден!"
print("Все добавленные элементы найдены ✓")

# Проверяем поиск отсутствующих элементов
for v in [5, 15, 33, 99, 100, -10]:
    assert find(v, root) is False, f"Элемент {v} ошибочно найден!"
print("Отсутствующие элементы корректно не найдены ✓")

# Проверка на пустом дереве
empty = Node(42)
assert find(42, empty) is True
assert find(43, empty) is False
print("Проверка граничных случаев пройдена ✓")

print("\nВсе проверки пройдены успешно!")