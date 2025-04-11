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

def draw_blot(x, y, color, saize=random.randrange(10, 20)):
    pygame.draw.circle(dis, color, [x, y], saize)

pygame.init()

dis = pygame.display.set_mode((800, 600))

dis.fill(TAN)

play = True

while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
            
    draw_blot(10, 20, RED)
    
    pygame.display.update()
            
pygame.quit()

quit()