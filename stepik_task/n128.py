s = "ножницы бумага камень ящерица Спок ножницы бумага камень ящерица Спок".split()

i = s.index(input())

contenders = [["ничья", s[i]], ["Тимур", s[i + 1], s[i + 3]], ["Руслан", s[i + 2], s[i + 4]]]
key = input()

for el in contenders:
    
    if key in el:
        
        print(el[0])
        
        break
    
    
    