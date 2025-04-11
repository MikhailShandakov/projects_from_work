from fractions import Fraction

n = int(input())

fraction_numbers = []

for i in range(1, n // 2 + n % 2):
    num = Fraction(i, n - i)
    if (i, n - i) == num.as_integer_ratio():
        fraction_numbers.append(num)
    
print(max(fraction_numbers))