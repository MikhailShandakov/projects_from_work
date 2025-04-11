a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 > a2:
    a1, b1, a2, b2 = a2, b2, a1, b1
    
if b1 == a2:
    print(a2)
    
elif b1 > b2:
    print(a2, b2)
    
elif b1 < a2:
    print("пустое множество")
    
else:
    print(a2, b1)