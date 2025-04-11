import pygame
import random

FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()


clock = pygame.time.Clock()
dis = pygame.display.set_mode((800, 600))
dis.fill(white)



pygame.display.update()

jump_height = 560
x1_block = 400
y1_block = 550

size_block_X = 20
size_block_Y = 20

motion = "STOP"
jump = "STOP"
game_over = False
play = True

while play:
    
    if motion == "LEFT" and x1_block > 0:
        x1_block -= 3
        
    elif motion == "RIGHT" and x1_block < 780:
        x1_block += 3
        
        
    if jump == "UP":
        y1_block -= 2
        
    if y1_block < jump_height:
        jump = "DOWN"
        
    if jump == "DOWN":
        y1_block += 2
        
    if y1_block == 580:
        jump = "STOP"
    
#     if y1_block > 580:
#         y1_block = 580
        
        
    
    
    
    dis.fill(white)
    
    block = pygame.draw.rect(dis, black, [x1_block, y1_block, size_block_X, size_block_Y])
    
    pygame.display.update()
    
    clock.tick(FPS)
    
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = "LEFT"
                
            elif i.key == pygame.K_RIGHT:
                motion = "RIGHT"
                
            elif i.key == pygame.K_UP and y1_block == 580:
                jump = "UP"
                
            elif i.key == pygame.K_DOWN:
                y1_block += 5
                x1_block -= 5
                size_block_X = 30
                size_block_Y = 15
                
        if i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                motion = "STOP"
                
            if i.key == pygame.K_DOWN:
                y1_block -= 5
                x1_block += 5
                size_block_X = 20
                size_block_Y = 20
                
            
        if i.type == pygame.QUIT:
            pygame.quit()
            play = False
            
    