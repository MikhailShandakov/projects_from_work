step = int(input())

cod = input()

for c in cod:
    ind = ord(c) - 97 - step
    if ind < 0:
        ind = 26 + ind
    print(chr(ind + 97), end='')