def have_fun(f, n):
    
    res = 0

    i = 0

    while n:
    
        res += (n % 10) * f ** i
    
        n //= 10
    
        i += 1
        
    return res

print(have_fun(2, 111111))