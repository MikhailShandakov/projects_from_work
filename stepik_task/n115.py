text = input("введите текст: ")

def detect_language(txt):
    
    english = False
    russian = False
    
    en_char_1 = [chr(65 + i) for i in range(26)]
    en_char_2 = [chr(97 + i) for i in range(26)]
    ru_char = [chr(1040 + i) for i in range(64)]
    
    for c in txt:
        if not c.isalpha():
            continue
        else:
            if c in en_char_1 + en_char_2:
                english = True
                
            elif c in ru_char:
                russian = True
                
    if ((english and russian) or
        (not english and not russia)):
        
        return "ОШИБКА"
    
    elif english:
        return en_char_1 + en_char_2
    
    elif russian:
        return ru_char
        
        