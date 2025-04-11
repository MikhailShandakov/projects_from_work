def do_caps_store(txt):
    
    return [i for i in range(len(txt)) if txt[i].isupper()]


def encryption(txt, step):
    
    result = ""
    
    for c in txt.lower():
        if c.isalpha():
            order = ord(c) + step
            
            if order > 122:
                order -= 26
                
            c = chr(order)
            
        result += c
        
    return result

def capitals_back(txt, cap):
    
    for i in range(len(txt)):
        if i in cap:
            txt = txt[:i] + txt[i].upper() + txt[i + 1:]
            
    return txt


text = input() + "."

result = ""
word = ""

for c in text:
    
    if c.isalpha():
        word += c
    else:
        caps = do_caps_store(word)
        new_word = encryption(word, len(word))
        cryptic_word = capitals_back(new_word, caps)
        
        result += cryptic_word
        result += c
        
        word = ""

print(result[:-1])