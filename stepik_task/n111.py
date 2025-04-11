import pygame
import random

FPS = 60

WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
GREEN = (20, 40, 10)
YELLOW = (225, 225, 10)
RED = (225, 80, 10)

pygame.init()

dis = pygame.display.set_mode((200, 600))

dis.fill(GREEN)

pygame.display.update()

play = True

while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
            
pygame.quit()

quit()