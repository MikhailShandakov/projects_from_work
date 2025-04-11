import pygame
import random

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (5, 5, 230)
GREY = (225, 225, 225)
PINK = (230, 50, 230)
YELLOW = (247, 236, 63)
INDIGO = (29, 44, 59)
BROWN = (65, 41, 25)

pygame.init()

dis = pygame.display.set_mode((800, 600))


def rock(x, y):
    
    pygame.draw.rect(dis, BROWN, [[x, y], [30, 30]])


def circ(x, y):
    
    pygame.draw.circle(dis, YELLOW, [x, y], 18)
    
clock = pygame.time.Clock()
    

# dis.fill(BLUE)
# 
# polygon = pygame.draw.polygon(dis, WHITE, [[100, 70], [630, 110], [700, 220], [70, 200], [400, 150]])
# line = pygame.draw.aalines(dis, WHITE, True, [[100, 70], [630, 110], [700, 220], [70, 200], [400, 150]])
# pygame.display.update()

x_rock = random.randrange(750)
y_rock = random.randrange(650)

x_circ = random.randrange(50, 750)
y_circ = random.randrange(50, 650)

x_rock_change = 1
y_rock_change = 1

x_circ_change = -1
y_circ_change = -1

play = True
while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    dis.fill(INDIGO)
            
    rock(x_rock, y_rock)
    
    circ(x_circ, y_circ)
    
    pygame.display.update()
    
    clock.tick(FPS)
    
    
    x_rock += x_rock_change
    
    if x_rock > 770:
        x_rock_change = -1
    elif x_rock < 1:
        x_rock_change = 1
        
        
    y_rock += y_rock_change
    
    if y_rock > 670:
        y_rock_change = -1
    elif y_rock < 1:
        y_rock_change = 1


    x_circ += x_circ_change
    
    if x_circ > 789:
        x_circ_change = -1
    elif x_circ < 9:
        x_circ_change = 1
    
    
    y_circ += y_circ_change
    
    if y_circ > 589:
        y_circ_change = -1
    elif y_circ < 9:
        y_circ_change = 1
    
    
            
            
pygame.quit()

quit()
