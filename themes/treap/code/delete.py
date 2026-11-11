from merge import merge


def delete(a, x):
    """Удалить из Treap узел с ключом x, если он есть.

    Возвращает корень изменённого дерева.
    """
    if a is None:
        return None

    if x == a.x:
        return merge(a.left, a.right)

    if x < a.x:
        a.left = delete(a.left, x)
    else:
        a.right = delete(a.right, x)
    return a
