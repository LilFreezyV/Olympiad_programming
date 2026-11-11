def split(a, k):
    """Разделить Treap на ключи <= k и ключи > k."""
    if a is None:
        return None, None

    if a.x > k:
        left, a.left = split(a.left, k)
        return left, a
    else:
        a.right, right = split(a.right, k)
        return a, right
