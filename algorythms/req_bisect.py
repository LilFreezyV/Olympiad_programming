def req_bisect(a, k, lo, hi):
    if hi - lo < 1: return a[lo] == k
    m = (lo + hi) // 2
    if a[m] == k:
        return True
    if a[m] > k:
        return req_bisect(a, k, lo, m - 1)
    else:
        return req_bisect(a, k, m + 1, hi)


# arr = [1, 2, 3, 5, 6, 7, 8, 9, 17, 45, 67]
# print(req_bisect(arr, 5, 0, len(arr)))