import pygame
import time
import random

pygame.init()

snake_block = 50
speed = snake_block // 2
    
FPS = 15
clock = pygame.time.Clock() 


# цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Размер окна
width = 800
height = 600

dis = pygame.display.set_mode((width, height))

pygame.display.update()  # Обновляем экран

pygame.display.set_caption("ЗМЕЙКА АСГ")  # Название

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 10, height / 3])
    

def gameLoop():
    # координаты змейки
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    
    lenght_snake = 1
    trek = []
    
    foodx = round(random.randrange(0, (width - snake_block) / 10) * 10)
    foody = round(random.randrange(0, (height - snake_block) / 10) * 10)
    
    
    start_menu = True  # Стартовое меню
    play = True  # Игра запущена
    
    while play:
        while start_menu:
            dis.fill(white)
            message("нажмите С для начала игры или Q для выхода", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_menu = False
                    play = False
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        start_menu = False
                        play = False
                        
                    elif event.key == pygame.K_c:
                        start_menu = False
                        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                play = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -speed
                    y1_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    x1_change = speed
                    y1_change = 0
                    
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -speed
                    
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = speed
                    
        trek.append((x1, y1))
                    
        x1 += x1_change
        y1 += y1_change
        
        
#   Врезание в стены:        
#         if x1 < 0 or (x1 + snake_block) > width or y1 < 0 or (y1 + snake_block) > height:
#             message("Вы проиграли!", red)
#             pygame.display.update()
#             time.sleep(3)
#             gameLoop()


        if x1 < 0:
            x1 = width - snake_block
        elif x1 > width - snake_block:
            x1 = 0
        
        if y1 < 0:
            y1 = height - snake_block
        elif y1 > height - snake_block:
            y1 = 0
        
        if ((foodx <= x1 <= foodx + snake_block and foody <= y1 <= foody + snake_block) or
            (foodx <= x1 + snake_block <= foodx + snake_block and foody <= y1 + snake_block <= foody + snake_block)):
            
            foodx = round(random.randrange(0, (width - snake_block) / 10) * 10)
            foody = round(random.randrange(0, (height - snake_block) / 10) * 10)
            
            lenght_snake += 1
        
        
        
        dis.fill(white)  # цвет фона
        
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        if lenght_snake > 1:
            for i in range(1, lenght_snake):
                pygame.draw.rect(dis, black, [trek[-i][0], trek[-i][1], snake_block, snake_block])
        
        pygame.display.update()
        
        clock.tick(FPS)
    
    pygame.quit()

    quit()
    
gameLoop()