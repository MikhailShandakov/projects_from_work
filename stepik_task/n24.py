password=input("Придумайте пароль")
while len(password)<7:
    print("Short")
    break

    chek=input("Введите пароль повторно")
    if chek!=password:
        print("Difference")
    else:
        print("OK")
