def bisect(a, k):
    l = 0
    r = len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] > k:
            r = m
        else:
            l = m + 1
    return l


a = [1, 2, 4, 5, 6, 7, 8, 9, 12, 54, 565]
print(bisect(a, 10))
