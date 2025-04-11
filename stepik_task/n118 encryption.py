def is_ru(txt):
    
    ru_char = [chr(1040 + i) for i in range(64)]
    en_char = [chr(65 + i) for i in range(26)] + [chr(97 + i) for i in range(26)]
    
    ru = len([c for c in txt if c in ru_char])
    en = len([c for c in txt if c in en_char])
    
    return ru > en


def do_caps_store(txt):
    
    return [i for i in range(len(txt)) if txt[i].isupper()]


def encryption(txt, step, ru):
    
    result = ""
    
    for c in txt.lower():
        if c.isalpha():
            
            if is_ru(c) and ru:
                order = ord(c) + step
                if order > 1103:
                    order -= 32
                c = chr(order)
                    
            elif not is_ru(c) and not ru:
                order = ord(c) + step
                if order > 122:
                    order -= 26
                c = chr(order)
                
        result += c
        
    return result

     
def decryption(txt, step, ru):
    
    result = ""
    
    for c in txt.lower():
        if c.isalpha():
            if is_ru(c) and ru:
                order = ord(c) - step
                if order < 1072:
                    order += 32
                c = chr(order)
                    
            elif not is_ru(c) and not ru:
                order = ord(c) - step
                if order < 97:
                    order += 26
                c = chr(order)
            
        result += c
        
    return result


def capitals_back(txt, cap):
    
    for i in range(len(txt)):
        if i in cap:
            txt = txt[:i] + txt[i].upper() + txt[i + 1:]
            
    return txt


text = input("t e x t : ")

print()

caps_store = do_caps_store(text)
ru = is_ru(text)

if ru:
    n = 32
else:
    n = 26
    
for i in range(n + 1):
    
    encrypt = encryption(text, i, ru)
    decrypt = decryption(text, i, ru)
    
    space = ""
    if i < 10:
        space = " "
        print(end=' ')
    if i == 0:
        space = "  "
        
    print(i, " : ",  capitals_back(encrypt, caps_store), "    *    ", space, -i, " : ", capitals_back(decrypt, caps_store))