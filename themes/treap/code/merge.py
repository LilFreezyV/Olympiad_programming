def merge(a, b):
    """Объединить Treap, если все ключи a меньше ключей b.

    Предполагается max-heap по приоритету y.
    """
    if a is None:
        return b
    if b is None:
        return a

    if a.y > b.y:
        a.right = merge(a.right, b)
        return a
    else:
        b.left = merge(a, b.left)
        return b
