n = int(input())

matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(abs(i - j))
    matrix.append(row)
    
for el in matrix:
    print(*el)