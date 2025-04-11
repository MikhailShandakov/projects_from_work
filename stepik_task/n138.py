n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
maximal_element = matrix[-1][-1]
for i in range(n):
    for j in range(n - 1 - i, n):
        if maximal_element < matrix[i][j]:
            maximal_element = matrix[i][j]
            

print(maximal_element)        