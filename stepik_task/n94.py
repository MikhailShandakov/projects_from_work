n = int(input())

while n > 9:
    k = 0
    while n > 0:
        k += n % 10
        n = n // 10
        
    n = k
    
print(n)