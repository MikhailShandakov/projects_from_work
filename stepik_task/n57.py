s, n = "*", int(input())

for i in range(n*19):
    s += "*"
    if i >=19 and i%19 == 0:
        s += "\n"

print(s)

