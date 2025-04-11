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
    dis.fill(BLACK)

    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                
        pygame.draw.circle(dis, RED, [X + 5, Y], 10)
        pygame.draw.circle(dis, RED, [X + 15, Y], 4)
        pygame.draw.rect(dis, GRAY, [X - 5, Y, 15, 20])
        pygame.draw.line(dis, BLACK, [X - 3, Y + 4], [X + 2, Y + 4])
        pygame.draw.line(dis, BLACK, [X + 15, Y - 4], [X + 15, Y])
                
        pygame.display.update()
            
    pygame.quit()
    
    quit()


gameloop()