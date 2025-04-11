#Сравнить три числа, вывести наибольшее

peak=int(input()) #Пик - наивысшая точка
hill=int(input())
if peak>hill: #Если пик выше, то это нормально
    pass       #Ничего не делаем
else:       
    peak=hill #Если нет, то пик был не тот

vale=int(input())  #Еще одна переменчивая Долина

if peak>vale:     #Пик все еще выше? Ок
    pass
else:
    peak=vale       #Нет? меняем значение
    
print(peak)          #Принтим
