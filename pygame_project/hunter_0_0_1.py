import pygame
import random

FPS = 60

WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
GREEN = (20, 40, 10)

YELLOW = (47, 213, 60)
RED = (200, 14, 19)
TAN = (252, 238, 209)
OO = (255, 221, 166)
GRANDIS = (255, 211, 140)
PURPLE = (125, 60, 255)
PURPLE_HEAD = (54, 0, 163)

def draw_blot(x, y, color, saize=random.randrange(5, 10)):
    pygame.draw.circle(dis, color, [x, y], saize)

background_dict = {i: {j: (random.randrange(j, j + 10), random.randrange(i, i + 10)) for j in range(0, 800, 15)} for i in range(0, 600, 20)}
pygame.init()

dis = pygame.display.set_mode((800, 600))

dis.fill(GRANDIS)

play = True

while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
    for d in background_dict.values():
        for x, y in d.values():
            draw_blot(x, y, OO)
    draw_blot(10, 20, RED)
    
    pygame.display.update()
            
pygame.quit()

quit()