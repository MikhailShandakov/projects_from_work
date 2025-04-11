#a^5+b^5+c^5+d^5=e^5
import sys

for e in range(150, 3, -1):
    
    for a in range(1, e):
        
        b_max = int((e ** 5 - a ** 5 - 2) ** 0.2)
        
        for b in range(1, b_max+1):
            
            c_max = int((e ** 5 - a ** 5 - b ** 5 - 1) ** 0.2)
            
            
            for c in range(1, c_max + 1):
                
                d = int((e ** 5 - a ** 5 - b ** 5 - c ** 5) ** 0.2)
                
                if e ** 5 == a ** 5 + b ** 5 + c ** 5 + d ** 5:
                    
                    print(a, b, c, d, e, sep=' + ', end=' = ')
                    print(a + b + c + d + e)
                    
                    sys.exit()
                
                    