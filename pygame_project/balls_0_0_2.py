import pygame
import random

FPS = 120

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

WIDTH = 200
HEIGHT = WIDTH

RADIUS = 10
DIAMETER = RADIUS + RADIUS

MOVE = 2
K = 8

pygame.init()

dis = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def circ(x, y):
    
    pygame.draw.circle(dis, YELLOW, [x, y], DIAMETER)
    
def badabum(x, y, rad, s):
    
    flag = False
    
    x1 = x - rad
    x2 = x + rad
    y1 = y - rad
    y2 = y + rad
    
    for el in s:
        
        if x == el[0] and y == el[1]:
            continue
        
        if x1 < el[0] + rad + K < x2:
            if y1 < el[1] < y2:
                flag = True
                
        if x1 < el[0] - rad - K < x2:
            if y1 < el[1] < y2:
                flag = True
                
        if y1 < el[0] + rad + K < y2:
            if x1 < el[1] < x2:
                flag = True
                
        if y1 < el[0] - rad - K < y2:
            if x1 < el[1] < x2:
                flag = True
                
    return flag
            
    
qua_circ = 2

coordinates = [
    [random.randrange(RADIUS, WIDTH - RADIUS), random.randrange(RADIUS, HEIGHT - RADIUS)],
    [random.randrange(RADIUS, WIDTH - RADIUS), random.randrange(RADIUS, HEIGHT - RADIUS)]
    ]

moves = [
    [MOVE, -MOVE],
    [-MOVE, MOVE]
    ]

play = True
while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    dis.fill(INDIGO)
    
    for i in range(qua_circ):
        
        coordinates[i][0] += moves[i][0]
        coordinates[i][1] += moves[i][1]
        
        if coordinates[i][0] < RADIUS + K or coordinates[i][0] > WIDTH - RADIUS - K:
            
            moves[i][0] *= -1
            coordinates[i][0] += moves[i][0]
            
        if coordinates[i][1] < RADIUS + K or coordinates[i][1] > HEIGHT - RADIUS - K:
            
            moves[i][1] *= -1
            coordinates[i][1] += moves[i][1]
                
        if badabum(coordinates[i][0], coordinates[i][1], RADIUS, coordinates):
            
            moves[i][0] *= -1
            moves[i][1] *= -1
            coordinates[i][0] += moves[i][0]
            coordinates[i][1] += moves[i][1]
            
                
        circ(coordinates[i][0], coordinates[i][1])
        
    pygame.display.update()
    
    clock.tick(FPS)
    
pygame.quit()

quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
