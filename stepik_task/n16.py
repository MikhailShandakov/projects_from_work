#сравнить 4 числа и вывести строкой, сколько имеется совпадений

a=int(input())
b=int(input())
c=int(input())
d=int(input())
twin=0

if a==b:
    if a==c:
        if a==d:
            twin=4
        else:
            twin=3
    else:
        if a==d:
            twin=3
        else:
            twin=2
            





else:
    if b==c:
        if b==d:
            twin=3
        else:
            twin=2

    else:
        if c==d:
            twin=2

        else:
            twin=0

print(twin)
            
