n = int(input())

Sn = int(n * (n + 1) / 2)  # арифметическая сумма

Sn_list = [ *range(1, Sn + 1) ]  # список

for y in range(1 , n + 1):  # для каждой строчки
    for x in range(y):  
        print(Sn_list[x], end=' ')  # печатаем первые индексы в списке
        
    print()  # перенос строки
    del Sn_list[:(x + 1)]  # удаляем первые индексы