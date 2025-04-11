n = int(input())

k = n % 10

n = n // 10

flag = "YES"

while n > 0:
    if n % 10 < k:
        flag = "NO"
    
    k = n % 10
    
    n = n // 10
    
print(flag)