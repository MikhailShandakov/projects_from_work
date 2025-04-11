import random


def blend_characters(digits, letters_low, letters_up, punctuation, symbol):

    DIGITS = "0123456789" * digits + "10" * symbol
    LETTERS_LOW = "abcdefghijklmnopqrstuvwxyz" * letters_low + "iol" * symbol
    LETTERS_UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * letters_up + "LO" * symbol
    PUNCTUATION = "!#$%&*+-=?@^_" * punctuation
    
    return DIGITS + LETTERS_LOW + LETTERS_UP + PUNCTUATION               


def generate_password(quantity, lenght, chars):
    
    passwords = []
    
    for _ in range(quantity):
        
        variant = ""
        
        for _ in range(lenght):
            
            i = random.randrange(len(chars))
            
            variant += chars[i]
            
        passwords.append(variant)
        
    return passwords


while True:
    digits = input("Использовать цифры? ").lower() == "да"
    letters_low = input("Использовать маленькие буквы? ").lower() == "да"
    letters_up = input("Использовать большие буквы? ").lower() == "да"
    punctuation = input("Использовать символы? ").lower() == "да"
    symbol = input("Исключить неоднозначные символы? ").lower() == "нет"
    quantity = int(input("Введите количество паролей "))
    lenght = int(input("Укажите какой длины должен быть пароль "))
    
    if (digits or letters_low or letters_up or punctuation) and quantity > 0 and lenght > 0:
        break
    
    print("", "", "ошибка, не подходящие условия", "", "", sep="\n")
    

chars = blend_characters(digits, letters_low, letters_up, punctuation, symbol)

password_list = generate_password(quantity, lenght, chars)

print(*password_list, sep="\n")