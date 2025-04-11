n = int(input())

for y in range(n):
    print(*range(1, y + 2), sep='', end='')
    print(*range(y, 0, -1), sep='')
