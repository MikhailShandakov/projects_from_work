n = 3
numbers = [i for i in range(1, n**2 + 1)]
matrix = []
matrix = [[int(num) if int(num) in numbers else "NO" for num in [4, 9, 2]] for _ in range(n)]
print(matrix)