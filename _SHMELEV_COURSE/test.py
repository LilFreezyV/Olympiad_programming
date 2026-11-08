n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

res = 0
was = set()
for i in range(n):
    for j in range(i + 1, n):
        x1, x2 = arr[i][0], arr[j][0]
        y1, y2 = arr[i][1], arr[j][1]
        if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0:
            x_c = (x1 + x2) // 2
            y_c = (y1 + y2) // 2
            if [x_c, y_c] in arr and (x_c, y_c) not in was:
                res += 1
                was.add((x_c, y_c))
print(res)
