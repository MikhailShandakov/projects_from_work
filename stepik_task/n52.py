x = float(input("Введите число"))

from math import copysign

sum = int(x) + x

while sum - int(sum) != 0:
    sum += copysign(0.01, x)
    sum = round(sum, 2)

print(sum)


