for a in range(1, 151):
    print(a)
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                E = a ** 5 + b ** 5 + c ** 5 + d ** 5
                
                e = int(E ** 0.2)
                
                if E == e ** 5:
                    print(a, b, c, d, e)
                    break
                
                
            else:
                continue
            
            break
            
        else:
            continue
        
        break
        
    else:
        continue
    
    break