def q_sort(l1, r1, arr):
    m = (l1 + r1) // 1
    l = l1
    r = r1
    pivot = arr[m]
    while True:
        while arr[l] < pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        else:
            return arr
            break