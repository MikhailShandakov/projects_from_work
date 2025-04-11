i = int(input())

list_7_17 = [range(1001, 10000, 7)] + [range(1003, 10000, 17)]

if i in list_7_17:
    print("YES")
else:
    print("NO")
