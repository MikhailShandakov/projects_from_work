import pygame
import random

FPS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (130, 30 , 20)
GREEN = (0, 255, 0)
BLUE = (5, 5, 230)
GREY = (225, 225, 225)
PINK = (230, 50, 230)
YELLOW = (220, 230 ,0)
BROWN = (70, 30, 20)


PIXEL = 10

width = PIXEL * 80
height = PIXEL * 60

pygame.init()

dis = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

dis.fill(BROWN)

pygame.display.update()

cicl = 0

count_worms = 1

x_worms = [[400]]
y_worms = [[300]]

len_worms = [1]

x_change = [-1]
y_change = [0]

move_set = ( ((0, -1), (0, -1), (1, 0), (0, -1)),
             ((0, -1), (0, -1), (-1, 0), (0, -1)),
             ((0, 1), (0, 1), (1, 0), (0, 1)),
             ((0, 1), (0, 1), (-1, 0), (0, -1)))
    

play = True
while play:
    cicl += 1
    if cicl == 4:
        cicl = 0
        
    dis.fill(BROWN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    for i in range(count_worms):
        
        x_change[i], y_change[i] = y_change[i], x_change[i]
        
        if x_worms[i][-1] >= width - PIXEL and x_change[i] != 0:
            x_change[i] = random.randint(-1, 1)
            if x_change[i] == 0:
                y_change[i] = random.choice([-1, 1])
                
        elif x_worms[i][-1] <= 0 and x_change != 0:
            x_change[i] = random.randint(0, 2)
            if x_change[i] == 0:
                y_change[i] = random.choice([-1, 1])
            
        if y_worms[i][-1] >= height - PIXEL and y_change[i] != 0:
            y_change[i] = random.randint(-1, 1)
            if y_change[i] == 0:
                x_change[i] = random.choice([-1, 1])
                
        elif y_worms[i][-1] <= 0 and y_change[i] != 0:
            y_change[i] = random.randint(0, 2)
            if y_change[i] == 0:
                x_change[i] = random.choice([-1, 1])
            
        
        new_point_x = x_worms[i][-1] + x_change[i] * PIXEL
        x_worms[i].append(new_point_x)
        
        new_point_y = y_worms[i][-1] + y_change[i] * PIXEL
        y_worms[i].append(new_point_y)
        
        if random.choice(range(len_worms[i])) == 0:
            len_worms[i] += 1
        
        for j in range(1, len_worms[i] + 1):
            pygame.draw.rect(dis, RED, [x_worms[i][-j], y_worms[i][-j], PIXEL, PIXEL])
            
    pygame.display.update()
    
    clock.tick(FPS)
    
pygame.quit()

quit()

clock = pygame.time.Clock()