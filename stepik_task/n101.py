n = int(input())

Odie = 0

for _ in range(n):
    s = input()
    if s.count("11") >= 3:
        Odie += 1
        
print(Odie)