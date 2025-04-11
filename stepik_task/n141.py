n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
answer = "YES"
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
            answer = "NO"
            
print(answer)