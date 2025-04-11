a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4*a*c

if D > 0:
    x1 = ((-b)+D**0.5) / (2*a)
    x2 = ((-b)-D**0.5) / (2*a)
    if x2 > x1:
        x1, x2 = x2, x1
    print(x2, x1, sep="\n")
    
elif D == 0:
    x = (-b) / (2*a)
    print(x)
    
else:
    print("Нет корней")
