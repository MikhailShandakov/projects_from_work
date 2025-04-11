def solve(f, n):
    
    res, i = 0, 0
    while n:
        res += (n % 10) * f ** i
        n //= 10
        i += 1
    return res


def test(f, res, arg1, arg2, arg3, arg4):
    
    result = solve(f, res)
    
    argument1 = solve(f, arg1)
    argument2 = solve(f, arg2)
    argument3 = solve(f, arg3)
    argument4 = solve(f, arg4)
    
    return result == argument1 + argument2 + argument3 + argument4


x, a, b, c, d = 88, 32, 22, 16, 17

for i in range(20):
    if test(i, x, a, b, c, d):
        print(i)
        break
    
print("X")