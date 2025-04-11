ru_char = [chr(1040 + i) for i in range(64)]
en_char = [chr(65 + i) for i in range(26)] + [chr(97 + i) for i in range(26)]
    
def is_ru(txt):
    
    i = [c for c in txt if c in ru_char]
    return len(i) > 0

def is_en(txt):
    
    i = [c for c in txt if c in en_char]
    return len(i) > 0

def valid(txt):
    
    i = is_ru(txt) + is_en(txt)
    return i == 1

def do_caps_store(txt):
    
    global caps_store
    caps_store = [i for i in range(len(txt)) if txt[i].isupper()]


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
     
def decryption(txt, step, ru, en):
    
    result = ""
    
    for c in txt.lower():
        if c.isalpha():
            order = ord(c) - step
            
            if ru and order < 1072:
                order += 32
            elif en and order < 97:
                order += 26
                
            c = chr(order)
            
        result += c
    
    return result

def capitals_back(txt):
    
    for i in range(len(txt)):
        if i in caps_store:
            txt = txt.replace(txt[i], txt[i].upper())
            
    return txt
    
while True:
    print("Введите текст для шифрование или дешифрования")
    print("текст должен быть только на русском или только на английском языке")
    
    text = input(">>> ")
    
    if valid(text):
        break
    print()
    
ru = is_ru(text)
en = is_en(text)
do_caps_store(text)
    
while True:
    print("ввести шаг сдвига")
    print("шаг целое число не превышающее количество букв в алфавите")
    
    step = int(input(">>> "))
    
    if (is_ru(text) and step > 32) or (is_en(text) and step > 26) or step < 1:
        print("некоректное число сдвига, попробуйте заново", end=" ")
        continue
        
    break

print("Исходный текст:", text)
print("Шаг сдвига:", step)
print()
print("Зашифрованный текст:", capitals_back(encryption(text, step, ru, en)))
print()
print("Дешифрованный текст:", capitals_back(decryption(text, step, ru, en)))
        
    
    