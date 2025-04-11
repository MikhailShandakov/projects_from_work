total = 1
for i in range(10):
    n = int(input())
    total *= n+(n==0)

print(total)
