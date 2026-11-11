def size(a):
    return a.size if a is not None else 0


def kth(a, k):
    """Вернуть ключ с индексом k в отсортированном порядке (индексация с нуля)."""
    if a is None or k < 0 or k >= a.size:
        raise IndexError("k вне диапазона")

    left_size = size(a.left)

    if k < left_size:
        return kth(a.left, k)
    if k == left_size:
        return a.x
    return kth(a.right, k - left_size - 1)
