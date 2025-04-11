n = int(input())

s_1 = 0

s_2 = 0

for i in range(n):
    k = int(input())
    if k>s_1:
        s_1, s_2 = k, s_1
    elif k>s_2:
        s_2 = k
        
print(s_1, s_2, sep = "\n")
