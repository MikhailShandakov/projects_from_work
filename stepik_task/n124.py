def good_luck(f, n):
    
    res = []
    
    while n >= f:
        
        ones = n % f

        res.insert(0, ones)

        n //= f
        
    res.insert(0, n)

    return res

print(good_luck(16, 1000))