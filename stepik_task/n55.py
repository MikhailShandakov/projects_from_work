from math import modf, copysign

x = float(input())

s = modf(x)

res = s[1]*2

if s[0] != 0:
    res += copysign(1, x)

print(res)
