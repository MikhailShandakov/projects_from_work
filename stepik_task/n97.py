n = int(input())

res = ''

while n > 0:
    i = n % 2
    res = str(i) + res
    n //= 2
    
print(res)