SIDE = ["Верхняя четверть:", "Правая четверть:", "Нижняя четверть:", "Левая четверть:"]

def sieve(matrix, n):
    
    left = []
    
    for i in range(n):
        for j in range(n):
            if i == j or i == n - 1 - j:
                break
            left.append(matrix[i][j])
            
    return sum(left)
            
def do_turn(matrix, n):
    
    new_matrix = []
    
    for i in range(1, n + 1):
        col = []
        for j in range(n):
            col.append(matrix[j][-i])
        new_matrix.append(col)
        
    return new_matrix


n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

for side in SIDE:
    matrix = do_turn(matrix, n)
    print(side, sieve(matrix, n))

