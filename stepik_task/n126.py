import random

word_list = '''струна приют принц аккомпанемент ртуть лицо строгий образование отступать японец
ложить колун гнев высочество исправлять компетентный негатив престол изменять консилиум'''.split()






























def get_word():
    return random.choice(word_list).lower()

def display_hangman(tries):
    
    line_1 = "--------"
    line_2 = "|      |"
    line_3 = "|       "
    line_4 = "|       "
    line_5 = "|       "
    line_6 = "|       "
    line_7 = "-       "
    
    if tries < 6:
        line_3 = "|      ۝"
    if tries < 5:
        line_4 = "|      ▀"
        line_5 = "|     ꜞ█ꜞ"
    if tries < 4:
        line_4 = "|     ▐▀"
    if tries < 3:
        line_4 = "|     ▐▀▌"
    if tries < 2:
        line_6 = "|      ─"
    if tries < 1:
        line_6 = "|      ∏"
        
    print(line_1, line_2, line_3, line_4, line_5, line_6, line_7, sep="\n")
    
    
def chek(word):
    
    ru_char = [chr(i) for i in range(1072, 1072 + 32)]
    
    flag = False
    
    while True:
        
        answer = input("угадать букву или слово целиком:  ").lower()
        
        if answer.isalpha():
            if len(answer) == 1:
                if answer in ru_char:
                    if answer in word:
                        flag = True
                    break
                  
            elif len(answer) > 1:
                if [c for c in answer if c not in ru_char]:
                    continue
                if answer == word:
                    flag = True
                break
                
    return flag, answer
                    

def play(word):
    
    word_completion = "_" * len(word)
    quessed = False
    quessed_letters = []
    quessed_words = []
    tries = 6
    
    print("Давайте играть в угадайку слов!")
    
    display_hangman(tries)
    
    print(word_completion)
    
    while True:
        
        flag, answer = chek(word)
        n = len(answer)
        
        if answer == word:
            print("Вы угадали слово! Поздравляем!")
            break
        
        if answer in quessed_letters:
            print("Такую букву уже называли!, попробуйте еще раз ")
            continue
        if answer in quessed_words:
            print("Такое слово уже называли!, попробуйте еще раз ")
            continue
        
        if flag == False:
            tries -= 1
            
            display_hangman(tries)
            
            if tries < 1:
                print("Вы проиграли")
                print("Загаданное слово", word)
                break
            
        else:
            if n == 1:
                quessed_letters.append(answer)
                
                word_completion = ''.join([c * (c in quessed_letters) + "_" * (c not in quessed_letters) for c in word])
                
                print()
                print(word_completion)
                print()
                
                if word_completion == word:
                    print("Вы собрали всё слово целиком! Поздравляем!")
                    break
            elif n > 1:
                quessed_words.append(answer)
                
                

secret_word = get_word()  

play(secret_word)