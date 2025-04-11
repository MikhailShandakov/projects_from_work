f = int(input("основание системы\n"))

n = input()

n_new = 0

for i in range(1, len(n) + 1):
    
    if n[i - 1].isalpha():
        k = 65
        while n[i - 1] != chr(k):
            k += 1
            
        a = k - 55
        
    else:
        a = int(n[i - 1])
        
    n_new += a * f ** (len(n) - i)
    
print(n_new)