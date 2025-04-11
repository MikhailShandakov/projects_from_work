lst = input().split()

n = int(input())

result = []

for i in range(n):
    result.append([])
    for j in range(len(lst)):
        if (j - i) % n == 0:
            result[i].append(lst[j])
            
print(result)