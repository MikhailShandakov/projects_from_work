def encryption(txt, step, ru, en):
    
    result = ""
    
    for c in txt.lower():
        if c.isalpha():
            order = ord(c) + step
            
            if ru and order > 1103:
                order -= 32
            elif en and order > 122:
                order -= 26
                
            c = chr(order)
            
        result += c
        
    return result

def do_caps_store(txt):
    
    global caps_store
    caps_store = [i for i in range(len(txt)) if txt[i].isupper()]
    
def capitals_back(txt):
    
    for i in range(len(txt)):
        if i in caps_store:
            txt = txt.replace(txt[i], txt[i].upper())
            
    return txt


text = "Блажен, кто верует, тепло ему на свете!"

do_caps_store(text)

crypt = encryption(text, 10, True, False)



print(capitals_back(crypt))