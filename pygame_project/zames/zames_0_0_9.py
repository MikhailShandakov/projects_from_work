import pygame
import random


FPS = 60

WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
GREEN = (20, 40, 10)
YELLOW = (47, 213, 60)
RED = (200, 14, 19)
TAN = (252, 238, 209)
GRANDIS = (255,200,112)
PURPLE = (125, 60, 255)
PURPLE_HEAD = (54, 0, 163)
GRAY = (128, 128, 128)
BROWN = (102, 51, 0)

WIDTH = 800
HEIGHT = 1000

X, Y = WIDTH / 2, HEIGHT / 2


def do_stylus(lenght_stylus=20):
    mouse_x, mouse_y = map(lambda mouse, center: mouse - center, pygame.mouse.get_pos(), [X, Y])
    leg = (mouse_x ** 2 + mouse_y ** 2) ** 0.5
    if leg == 0:
        leg = 1
    x = lenght_stylus * mouse_x / leg + X
    y = lenght_stylus * mouse_y / leg + Y
    return x, y


def draw_stylus(surface, end, stylus_color=GRANDIS, start=[X, Y], width_stylus=4):    
    pygame.draw.line(surface, stylus_color, start, end, width_stylus)
       
       
       
def draw_character(surface, color_hair, color_body, color_elements=BLACK):
    
    if pygame.mouse.get_pos()[0] > WIDTH / 2:
        pygame.draw.circle(surface, color_hair, [X - 2, Y - 10], 10)
        pygame.draw.circle(surface, color_hair, [X - 12, Y - 10], 4)
        pygame.draw.rect(surface, color_body, [X - 8, Y - 10, 16, 20])
        pygame.draw.line(surface, color_elements, [X + 4, Y - 6], [X + 1, Y - 6])
        pygame.draw.line(surface, color_elements, [X - 12, Y - 14], [X - 12, Y - 10])
    else:
        pygame.draw.circle(surface, color_hair, [X + 2, Y - 10], 10)
        pygame.draw.circle(surface, color_hair, [X + 12, Y - 10], 4)
        pygame.draw.rect(surface, color_body, [X - 8, Y - 10, 16, 20])
        pygame.draw.line(surface, color_elements, [X - 4, Y - 6], [X - 1, Y - 6])
        pygame.draw.line(surface, color_elements, [X + 12, Y - 14], [X + 12, Y - 10])


def draw_trees(dict2):
    for tree_x, tree_y in dict2.values():
        pygame.draw.rect(dis, BROWN, [tree_x, tree_y, 10, 40])
        pygame.draw.circle(dis, GREEN, [tree_x + 5, tree_y], 20)
      
      
def do_bullets(bullets, *args):
    for key in bullets.copy():
        bullets[key] += bullets[key] / 10
        

def exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def gameloop():
    
    pygame.init()

    dis = pygame.display.set_mode((WIDTH, HEIGHT))
    
    shift_x = 0
    shift_y = 0
    
    up, down, left, right = False, False, False, False
    
    
    fire = False
    count = 1
    
    while True:
        if exit():
            break
        else:
            count += 1
        
        stylus = do_stylus()
        
        dis.fill(BLACK)
        draw_character(surface=dis, color_hair=RED, color_body=GRAY)
        draw_stylus(dis, stylus)        
        pygame.display.update()
        
    pygame.quit()
    
    quit()
    
gameloop()