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

WIDTH = 800
HEIGHT = 600

RADIUS = 15

MOVE = 1

pygame.init()

dis = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def circ(x, y):
    
    pygame.draw.circle(dis, YELLOW, [x, y], RADIUS)
    
def badabum(x, y, rad, s):
    
    flag = False
    
    for el in s:
        
        if el[2]:
            k1 = abs(x - el[0])
            k2 = abs(y - el[1])
            gypo = (k1 * k1 + k2 * k2) ** 0.5
            
            if 0 < gypo <= rad + rad:
                
                flag = True
            
    return flag
     
qua_circ = 2

coordinates = [
    [100, 100, "YELLOW"],
    [500, 500, "YELLOW"]
    ]

moves = [
    [1, 1],
    [-1, -1]
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
        
        if coordinates[i][0] < RADIUS or coordinates[i][0] > WIDTH - RADIUS:
                
                moves[i][0] *= -1
                coordinates[i][0] += moves[i][0]
                
        if coordinates[i][1] < RADIUS or coordinates[i][1] > HEIGHT - RADIUS:
                
                moves[i][1] *= -1
                coordinates[i][1] += moves[i][1]
                
        if coordinates[i][2]:
                    
            if badabum(coordinates[i][0], coordinates[i][1], RADIUS, coordinates):
                
                moves[i][0] *= -random.choice([0.9, 1.0, 1.1])
                moves[i][1] *= -random.choice([0.9, 1.0, 1.1])
                coordinates[i][0] += moves[i][0]
                coordinates[i][1] += moves[i][1]
                
                if coordinates[-1][2]:
                    qua_circ += 1
                    
                    coordinates.append([coordinates[i][0], coordinates[i][1], False])
                    moves.append([random.choice([-1, 1]), random.choice([-1, 1])])
                
        else:
            if not badabum(coordinates[i][0], coordinates[i][1], RADIUS, coordinates):
                coordinates[i][2] = True
         
        
        circ(coordinates[i][0], coordinates[i][1])
        
    pygame.display.update()
    
    clock.tick(FPS)
    
pygame.quit()

quit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
