import random

def gameloop():
    
    end = int(input("Задайте значение правой границы: "))
    
    n = random.randint(1, end)

    def is_valid(num):
        return num in range(1, end + 1)

    attempts = 0
    
    
    print(f"Угадайте число от 1 до {end}")

    while True:
        
        
        number = int(input())
        
        if not is_valid(number):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue
        
        if number == n:
            print("Вы угадали, поздравляем!")
            print(f" Количество попыток {attempts}")
            break
        
        attempts += 1
            
        if number > n:
            print("Ваше число больше загаданного, попробуйте еще разок")
            continue
        
        elif number < n:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            continue
        
    


print("Добро пожаловать в числовую угадайку")

while True:
    gameloop()
    
    if input("Напишите quit для выхода ") == "quit":
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break
    
    else:
        print("Новая игра")