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

def draw_blot(x, y, color, size=random.randrange(5, 10)):
    pygame.draw.circle(dis, color, [x, y], size)

background_dict = {i: {j: (random.randrange(j, j + 10), random.randrange(i, i + 10)) for j in range(0, 800, 45)} for i in range(0, 600, 20)}
pygame.init()

dis = pygame.display.set_mode((800, 600))

# dis.fill(GRANDIS)

x_shift, y_shift = 0, 0
x_mouse, y_mouse = -10, -10
v_x, v_y = 0, 0

play = True

while play:
    
    if not v_x:
        point_x = 400
    if not v_y:
        point_y = 300
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("click")
                v_x, v_y = 0, 0
                
                x_mouse, y_mouse = event.pos
                s_x = abs(400 - x_mouse)
                s_y = abs(300 - y_mouse)
                
                if s_x >= s_y:
                    t = s_x
                else:
                    t = s_y
                    
                if t != 0:
                    v_x = s_x / t
                    v_y = s_x / t
                    
                    if x_mouse > 400:
                        v_x *= -1
                    if y_mouse > 300:
                        v_y *= -1
                        
    x_shift += v_x
    y_shift += v_y
    
    point_x += v_x
    point_y += v_y
    
    if abs(point_x - x_mouse) < 2:
        v_x = 0
    if abs(point_y - y_mouse) < 2:
        v_y = 0
    
    for d in background_dict.values():
        for x, y in d.values():
            
            new_x = x + x_shift
            new_y = y + y_shift
         
            draw_blot(new_x, new_y, OO)
    
    
    draw_blot(400, 300, PURPLE_HEAD, size=5)
    
    pygame.display.update()
    
    dis.fill(GRANDIS)
    
pygame.quit()

quit()