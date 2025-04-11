n = int(input())

if n == 0:
    print("зеленый")
    
elif n > 36 or n < 0:
    print("ошибка ввода")

else:
    n = n + (n < 11) + (n > 28)
    

    if (n < 19 and n % 2 == 1) or (n > 18 and n % 2 == 0):
        print("черный")
        
    else:
        print("красный")
