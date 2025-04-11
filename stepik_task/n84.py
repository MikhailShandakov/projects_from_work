from math import sqrt

for a in range(1, 150):
    b_m = int((150 ** 5 - a ** 5 - 2) ** 0.2) + 1
    print(a , "-=-", b_m)
