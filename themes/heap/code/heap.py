a = [10, 6, 4, 5, 2, 3]


def add(x):
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[i] > a[(i - 1) // 2]:
        a[i], a[(i - 1) // 2] = a[(i - 1) // 2], a[i]
        i = (i - 1) // 2


def get():
    r = a[0]
    last = a.pop()
    if not a:                   # в куче был один элемент — он и был корнем
        return r
    a[0] = last
    i = 0
    while 2 * i + 1 < len(a):
        j = 2 * i + 1                                   # левый сын
        if j + 1 < len(a) and a[j + 1] > a[j]:
            j += 1                                      # правый больше — берём его
        if a[i] >= a[j]:
            break
        a[i], a[j] = a[j], a[i]                         # меняем с большим сыном
        i = j                                           # и идём именно к нему
    return r

print(a)
get()
print(a)



