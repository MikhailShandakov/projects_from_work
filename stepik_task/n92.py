# На вход программе подается два натуральных числа a и b. Напишите программу, которая находит натуральное число из отрезка
#[a;b] с максимальной суммой делителей и сумму его делителей. Если таких чисел несколько, то выведите наибольшее из них.

a, b = int(input()), int(input())

general = 0

general_division = 0

for i in range(a, b + 1):
    if i % 2 == 1:
        continue
    
    division = 0
    
    for j in range(1, i + 1):
        
        if i % j == 0:
            
            division += j
            
            
    if division >= general_division:
        general_division = division
        general = i
        
print(general, general_division)