n = int(input())

count = 1

for line in range(1, n + 1):
    for _ in range(line):
        print(count, end=' ')
        count += 1
        
    print()