#a^5+b^5+c^5+d^5=e^5
#допустим е=150
#тогда макс=150^5-3

a_m = int((150 ** 5 - 3) ** 0.2) + 1

for a in range(1, a_m):
    print("---------------============", a, "===========--------------------")
    b_m = int((150 ** 5 - a ** 5 - 2) ** 0.2) + 1
    for b in range(1, b_m):
        print("второй цикл", b)
        c_m = int((150 ** 5 - a ** 5 - b ** 5 - 1) ** 0.2) + 1
        for c in range(1, c_m):
            d_m = int((150 ** 5 - a ** 5 - b ** 5 - c ** 5) ** 0.2) + 1
            for d in range(1, d_m):
                e = (a ** 5 + b ** 5 + c ** 5 + d ** 5) ** 0.2
                print("e =", e)
                if e % 1 == 0.0:
                    print("YES", a, b, c, d, e, sep='\n')
                    exit