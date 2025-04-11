alphabet = [chr(i) for i in range(97, 123)]
temp=None
while True:
    temp=input()
    if alphabet in temp:
        print("Введите число")
    else:
        int(temp)
        if temp<-30:
            print("Сиди дома")
        else:
            print("Идти в школу")
