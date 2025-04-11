s = input()

count = -2

for i in range(len(s)):
    if s[i] == "f":
        count += 1
        
    if count == 0:
        print(i)
        break
        
else:
    print(count)



