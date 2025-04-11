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
    
    def get_stylus(mouse_x, mouse_y):
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

    play = True

    while play:
        
        pos = pygame.mouse.get_pos()
        
        stylus_x, stylus_y = get_stylus(pos[0], pos[1])
        
        
        if pos[0] > WIDTH / 2:
            reverse_character = True
            stylus_x = X + stylus_x
        else:
            reverse_character = False
            stylus_x = X - stylus_x
            
        if pos[1] > HEIGHT / 2:
            stylus_y = Y + stylus_y
        else:
            stylus_y = Y - stylus_y
            
        
        print(stylus_x, stylus_y)
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
                    
        
        dis.fill(BLACK)
        character(reverse_character)
        pygame.draw.line(dis, GRANDIS, [X, Y], [stylus_x, stylus_y], 4)
        pygame.draw.circle(dis, GRAY, [X, Y], 4)
        pygame.display.update()
            
    pygame.quit()
    
    quit()


gameloop()