n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]

for i in range(n):
    row = list(range(1, n + 1))
    col = list(range(1, n + 1))
    for j in range(n):
        a = matrix[i][j]
        b = matrix[j][i]
        if a in row:
            row.remove(a)
        if b in col:
            col.remove(b)
    if row or col:
        print("NO")
        break
else:
    print("YES")