m, n = int(input()), int(input())

list_17 = list(range(0, n+1, 17))

list_9 = list(range(9, n+1, 10))

list_3_5 = list(range(0, n+1, 15))

list_gen = sorted(list_17+list_9+list_3_5)

for i in list_gen:
    if i>=m:
        print(i)
