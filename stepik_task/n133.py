n, m = 4, 5

matrix = [[None] * m for _ in range(n)]
i, j = 0, 0
x = 1
end = n * m
while True:
    
    if x > end:
        break
    
    for j in range(j, m):
        matrix[i][j] = x
        x += 1
    
    i += 1
    
    if x > end:
        break
    
    for i in range(i, n):
        matrix[i][j] = x
        x += 1
        
    j -= 1
    
    n -= 1
    m -= 1
    
    if x > end:
        break
    
    for j in range(j, j - (m - 1) - 1, -1):
        matrix[i][j] = x
        x += 1
        
    
    if x > end:
        break
    
    i -= 1
    
    for i in range(i, i - (n - 1) - 1, -1):
        matrix[i][j] = x
        x += 1
        
    m -= 1
    
for row in matrix:
    print(*row)