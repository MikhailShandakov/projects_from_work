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

WIDTH = 800
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
    
qua_circ = 2

coordinates = [
    [random.randrange(RADIUS, WIDTH - RADIUS), random.randrange(RADIUS, HEIGHT - RADIUS)],
    [random.randrange(RADIUS, WIDTH - RADIUS), random.randrange(RADIUS, HEIGHT - RADIUS)]
    ]

moves = [
    [MOVE, MOVE],
    [-MOVE, -MOVE]
    ]

play = True
while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    dis.fill(INDIGO)
    
    for i in range(qua_circ):
        
        for j in range(2):
            
            coordinates[i][j] += moves[i][j]
            
            if coordinates[i][j] < RADIUS + K or coordinates[i][j] > WIDTH - RADIUS - K:
                
                moves[i][j] *= -1
                coordinates[i][j] += moves[i][j]
                
        circ(coordinates[i][0], coordinates[i][1])
        
    pygame.display.update()
    
    clock.tick(FPS)
    
pygame.quit()

quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
