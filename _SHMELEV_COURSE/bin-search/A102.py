n, m = map(int, input().split())
arr = list(map(int, input().split()))
req = []
for _ in range(m):
    req.append(int(input()))


def bisect(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return l

for r in req:
    b_ind = bisect(arr, r)
    print(b_ind)

