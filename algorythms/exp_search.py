from req_bisect import req_bisect


def exp_search(a, k):
    st = 1
    while st <= len(a) and a[st] < k:
        st *= 2
    st = min(len(a), st)
    return req_bisect(a, k, 0, st)


arr = [1, 2, 3, 4, 5, 6, 67, 77, 88, 99]
print(exp_search(arr, 99))
