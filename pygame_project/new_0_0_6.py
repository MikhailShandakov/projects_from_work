import pygame
import random


FPS = 60

WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
GREEN = (20, 40, 10)
YELLOW = (47, 213, 60)
RED = (200, 14, 19)
TAN = (252, 238, 209)
GRANDIS = (255,200,112)
PURPLE = (125, 60, 255)
PURPLE_HEAD = (54, 0, 163)
GRAY = (128, 128, 128)

WIDTH = 800
HEIGHT = 1000

X, Y = WIDTH / 2, HEIGHT / 2


def gameloop():
    
    pygame.init()

    dis = pygame.display.set_mode((WIDTH, HEIGHT))
    
    reverse_character = False
    
    shift_x = 0
    shift_y = 0
    
    up, down, left, right = False, False, False, False
    
    stylus = 20
    
    bullet_dict = {}
    
    def get_step(mouse_x, mouse_y):
        x = abs(X - mouse_x)
        y = abs(Y - mouse_y)
        b = (x ** 2 + y ** 2) ** 0.5
        p_1 = stylus * x / b
        p_2 = stylus * y / b
        
        return p_1, p_2
    
    def character(rev):
        if rev:
            pygame.draw.circle(dis, RED, [X - 2, Y - 10], 10)
            pygame.draw.circle(dis, RED, [X - 12, Y - 10], 4)
            pygame.draw.rect(dis, GRAY, [X - 8, Y - 10, 16, 20])
            pygame.draw.line(dis, BLACK, [X + 4, Y - 6], [X + 1, Y - 6])
            pygame.draw.line(dis, BLACK, [X - 12, Y - 14], [X - 12, Y - 10])
        else:
            pygame.draw.circle(dis, RED, [X + 2, Y - 10], 10)
            pygame.draw.circle(dis, RED, [X + 12, Y - 10], 4)
            pygame.draw.rect(dis, GRAY, [X - 8, Y - 10, 16, 20])
            pygame.draw.line(dis, BLACK, [X - 4, Y - 6], [X - 1, Y - 6])
            pygame.draw.line(dis, BLACK, [X + 12, Y - 14], [X + 12, Y - 10])
            
    def bullet(dict1):
        for bul_x, bul_y in dict1.values():
            pygame.draw.circle(dis, WHITE, [bul_x, bul_y], 4)

    count = 0
    play = True

    while play:
        count += 1
        
        pos = pygame.mouse.get_pos()
        
        step_x, step_y = get_step(pos[0], pos[1])
        
        if pos[0] > WIDTH / 2:
            reverse_character = True
            stylus_x = X + step_x
        else:
            reverse_character = False
            step_x *= -1
            stylus_x = X + step_x
            
        if pos[1] > HEIGHT / 2:
            stylus_y = Y + step_y
        else:
            step_y *= -1
            stylus_y = Y + step_y
        
        important_dict = bullet_dict.copy()
        for obj in important_dict:
            new_x = important_dict[obj][0] + obj[0] / 10
            new_y = important_dict[obj][1] + obj[1] / 10
            
            bullet_dict[obj] = [new_x, new_y]
            
            if not 0 < new_x < WIDTH or not 0 < new_y < HEIGHT:
                del bullet_dict[obj]
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
                    up, down, left, right = False, False, False, False
                    
                if event.key == pygame.K_UP:
                    up = True
                elif event.key == pygame.K_DOWN:
                    down = True
                elif event.key == pygame.K_LEFT:
                    left = True
                elif event.key == pygame.K_RIGHT:
                    right = True
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(bullet_dict)
                    bullet_dict[(step_x, step_y, count)] = [stylus_x, stylus_y]
        
        
        dis.fill(BLACK)
        character(reverse_character)
        pygame.draw.line(dis, GRANDIS, [X, Y], [stylus_x, stylus_y], 4)
        pygame.draw.circle(dis, GRAY, [X, Y], 4)
        bullet(bullet_dict)
        pygame.display.update()
            
    pygame.quit()
    
    quit()


gameloop()