a, b, c = map(int, input().split())
K = [0] * 7
for x in range(a):
    fx = (x == 0) + (x == a - 1)
    for y in range(b):
        fy = (y == 0) + (y == b - 1)
        for z in range(c):
            K[fx + fy + (z == 0) + (z == c - 1)] += 1
print(*K)