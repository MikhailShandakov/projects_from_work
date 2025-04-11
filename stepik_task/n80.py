n = int(input())

k = 0

for i in range(1, -2, -2):
    for _ in range(n, 0, -2):
        k += i
        print("*" * k)
        
    