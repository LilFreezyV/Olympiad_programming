a = [0, 3, 2, 5, 6, 1]
b = [0] * (len(a) + 1)
for i in range(len(a)):
    print(a[i])
    b[a[i]] = 1
print(b)
