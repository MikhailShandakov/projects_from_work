n = int(input())

total = 0

while n:
    k = 1
    for i in range(1, n + 1):
        k *= i
        
    total += k
    n -= 1
    
print(total)