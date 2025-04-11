import pygame
import random
import math


FPS = 60

WHITE = (240, 240, 240)
BLACK = (45, 45, 45)
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


def do_trees(trees_matrix, change):
    
    for row in trees_matrix:
        for col in row:
            col[0] += change[pygame.K_d] - change[pygame.K_a]
            col[1] += change[pygame.K_s] - change[pygame.K_w]
    
def draw_trees(surface, color_trunk, color_crown, trees_dict):
    for tree in trees_dict.values():
        tree_x, tree_y = tree["point"]
        pygame.draw.rect(surface, color_trunk, [tree_x, tree_y, 10, 40])
        pygame.draw.circle(surface, color_crown, [tree_x + 5, tree_y], 20)
      
      
def do_bullets(bullets, *args):
    for key in bullets.copy():
        bullets[key][0] += bullets[key][0] / 10
        bullets[key][1] += bullets[key][1] / 10
        for objects_dict in args:
            for obj in objects_dict:
                pass


def gameloop():
    
    pygame.init()

    dis = pygame.display.set_mode((WIDTH, HEIGHT))
    
    trees = {}    
    
    shift_x = 0
    shift_y = 0
    
    move_dict = {pygame.K_w: 0, pygame.K_s: 0, pygame.K_a: 0, pygame.K_d: 0}
    trees = [[0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]
             [0, 0, 0, 0, 0, 0, 0, 0]]
    
    fire = False
    count = 1
    play = True
    
    while play:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            elif event.type == pygame.KEYDOWN:
                move_dict[event.key] = 1
            elif event.type == pygame.KEYUP:
                move_dict[event.key] = 0

        count += 1
        do_trees(trees, move_dict)
        
        dis.fill(BLACK)
        draw_character(dis, color_hair=RED, color_body=GRAY)
        draw_stylus(dis, do_stylus())
        draw_trees(dis, color_trunk=BROWN, color_crown=GREEN, trees_dict=trees)
        pygame.display.update()
        
    pygame.quit()
    
    quit()
    
gameloop()