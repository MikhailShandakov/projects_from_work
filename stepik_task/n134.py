n, m = [int(num) for num in input().split()]

matrix = [[None] * m for _ in range(n)]
numbers = list(range(1, n * m + 1))

i, j = 0, 0
while numbers:
    
    for j in range(j, j + m):
        if numbers:
            matrix[i][j] = numbers.pop(0)
        
    i += 1
    n -= 1
        
    for i in range(i, i + n):
        if numbers:
            matrix[i][j] = numbers.pop(0)
        
    j -= 1
    m -= 1
    
    for j in range(j, j - m, -1):
        if numbers:
            matrix[i][j] = numbers.pop(0)
        
    i -= 1
    n -= 1
    
    for i in range(i, i - n, -1):
        if numbers:
            matrix[i][j] = numbers.pop(0)
        
    j += 1
    m -= 1
    
for row in matrix:
    for el in row:
        print(str(el).ljust(3), end="")
    print()
        
    