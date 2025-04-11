def my_range(get):
    s = []
    n = 0
    while n != get:
        s.append(n)
        n += 1
        
    return s

print(my_range(10))