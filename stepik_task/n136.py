def multi(m1, m2):
    
    n = len(m1)
    m = len(m1[0])
    
    r = len(m2)
    k = len(m2[0])
    
    if m != r:
        return []
    
    result = [[0] * k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for g in range(r):
                result[i][j] += m1[i][g] * m2[g][j]
    return result

n = int(input())

matrix1 = [[int(num) for num in input().split()] for _ in range(n)]

matrix2 = matrix1.copy()

for _ in range(int(input()) - 1):
    
    matrix2 = multi(matrix1, matrix2)
    
for el in matrix2:
    print(*el)

