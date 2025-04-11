#Полиндроп

n = input()

flag = True

for i in range(len(n)):
    if n[i] != n[-(i+1)]:
        flag = False
        
if flag == True:
    print("YES")
    
else:
    print("NO")