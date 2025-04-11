n = int(input())

for y in range(n):
    for x in range(1, y + 2):
        print(x, end='')
        
    for z in range(y, 0, -1):
        print(z, end='')
        
    print()