f = int(input("основание системы\n"))

n = int(input())

new_n = 0
i = 0

while n:
    
    new_n += (n % 10) * f ** i
    
    n //= 10
    
    i += 1
    
print(new_n)