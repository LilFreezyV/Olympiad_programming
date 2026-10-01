def sort(a, l, r):
    pi = 1
    pivot = a[pi]
    pv = a[1]
    li = l
    ri = r
    while a[li] < pivot:
        li += 1
    while a[ri] > pivot:
        ri -= 1
    if li < ri:
        a[li], a[ri] = a[ri], a[li]