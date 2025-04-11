n = 3

matrix = [[int(num) for num in input().split()] for _ in range(n)]

x = sum(matrix[0])

answer = "YES"

    


test_3 = 0

test_4 = 0

test_5 = [i for i in range(1, n ** 2)]
    
for i in range(n):
    
    test_1 = 0

    test_2 = 0

    for j in range(n):
        
        test_1 += matrix[i][j]
        test_2 += matrix[j][i]
        
        if matrix[i][j] in test_5:
            test_5.remove(matrix[i][j])
        
    if test_1 != x or test_2 != x:
        answer = "NO"
        break
        
    test_3 += matrix[i][i]
    test_4 += matrix[i][n - 1 - i]
    
print(test_5)
    
if test_3 != x or test_4 != x or test_5:
    answer = "NO"
    
print(answer)