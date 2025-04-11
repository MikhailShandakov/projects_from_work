def magic_square():
    n = int(input())
    numbers, matrix = [i in range(n**2 + 1)], []
    for _ in range(n):
        row = []
        for i in input().split():
            num = int(i)
            if num in numbers:
                row.append(numbers.pop(num))
            else:
                return "NO"
            
        matrix.append(row)
                
    if numbers != [0]:
        return "NO"
    
    total_1, total_2 = 0, 0
    for i in range(n):
        total_row, total_col = 0, 0
        total_1 += matrix[i][i]
        total_2 += matrix[i][n - 1 - i]
        for j in range(n):
            total_row += matrix[i][j]
            total_col += matrix[j][i]
        numbers.append(total_row)
        numbers.append(total_col)
    numbers.append(total_1)
    numbers.append(total_2)
    
    if sum(numbers) / (len(numbers) - 1) == numbers[-1]:
        return "YES"
    else:
        retern "NO"

