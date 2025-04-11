password="1990"
T=0

while True:
    answer=input("Введите пароль")
    T+=1
    if answer==password:
        print("Здраствуйте Хозяин")
        break
    if T==3:
        print("Попытки кончились")
        break
