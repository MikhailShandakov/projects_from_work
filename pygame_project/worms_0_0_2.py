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

x_change = 0
y_change = 0

move = 0
move_set = ( ((0, -1), (0, -1), (1, 0), (0, -1)),  # 0 вверх, сдвиг вправо
             ((0, -1), (0, -1), (-1, 0), (0, -1)),  # 1 вверх, сдвиг влево
             ((0, 1), (0, 1), (1, 0), (0, 1)),  # 2 вниз, сдвиг вправо
             ((0, 1), (0, 1), (-1, 0), (0, 1)),  # 3 вниз, сдвиг влево
             ((1, 0), (1, 0), (0, -1), (1, 0)),  # 4 вправо, сдвиг вверх
             ((1, 0), (1, 0), (0, 1), (1, 0)),  # 5 вправо, сдвиг вниз
             ((-1, 0), (-1, 0), (0, -1), (-1, 0)),  # 6 влево, сдвиг вверх
             ((-1, 0), (-1, 0), (0, 1), (-1, 0)),  # 7 влево, сдвиг вниз
             ((1, 0), (0, 1), (1, 0), (0, 1)),  # 8 вправо, вниз
             ((1, 0), (0, -1), (1, 0), (0, -1)),  # 9 вправо, вверх
             ((-1, 0), (0, 1), (-1, 0), (0, 1)),  # 10 влево, вниз
             ((-1, 0), (0, -1), (-1, 0), (0, -1)))  # 11 влево, вверх

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
        
        if x_worms[i][-1] >= width:
            move = random.choice([1, 3, 6, 7, 10, 11])
                
        elif x_worms[i][-1] <= 0:
            move = random.choice([0, 2, 4, 5, 8, 9])
            
        if y_worms[i][-1] >= height - PIXEL:
            move = random.choice([0, 1, 4, 6, 9, 11])
                
        elif y_worms[i][-1] <= 0:
            move = random.choice([2, 3, 5, 7, 8, 10])
            
        x_change, y_change = move_set[move][cicl]
        
        new_point_x = x_worms[i][-1] + x_change * PIXEL
        x_worms[i].append(new_point_x)
        
        new_point_y = y_worms[i][-1] + y_change * PIXEL
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