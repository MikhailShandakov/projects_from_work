#a^5+b^5+c^5+d^5=e^5
import sys
for e in range(1, 151):
    print(e)
    for a in range(1, e):
        for b in range(1, e):
                for c in range(1, e):
                        d = e ** 5 - a ** 5 - b ** 5 - c ** 5
                        
                        if e ** 5 == a ** 5 + b ** 5 + c ** 5 + d ** 5:
                            print(a,b,c,d,e)
                            sys.exit
                        