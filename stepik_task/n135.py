def change(row):
    for i in range(len(row)):  # Функция принимает строку с None
        global a
        if row[i] != None:     # Замена None на число
            a = row[i]
        else:
            row[i] = a + 1
            a += 1
            
    return row
            
            
def turn(matrix, n, m):  # Функция поворачивает матрицу
    
    new_matrix = []
    
    for j in range(1, m + 1):
        row = []
        for i in range(n):
            row.append(matrix[i][-j])
        new_matrix.append(row)
        
    return new_matrix, len(new_matrix), len(new_matrix[0])


x, y = [int(num) for num in input().split()]

matrix = [[None] * y for _ in range(x)]
matrix[0][0] = 1
a = 1

while True:
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        if None in matrix[i]:
            matrix[i] = change(matrix[i])
            break
    else:
        while not (matrix[0][0] == 1 and n == x and m == y):
            matrix, n, m = turn(matrix, n, m)
        break
    
    matrix, n, m = turn(matrix, n, m)
    
for row in matrix:
    print(*[str(num).ljust(3) for num in row])
    