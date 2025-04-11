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


def draw_stylus(surface, stylus_color, width_stylus):

    def trend(mouse_position: tuple, lenght_stylus=20):
        mouse_x, mouse_y = map(lambda mouse, center: mouse - center, mouse_position, [X, Y])
        leg = (mouse_x ** 2 + mouse_y ** 2) ** 0.5
        if leg == 0:
            leg = 1
        x = lenght_stylus * mouse_x / leg + X
        y = lenght_stylus * mouse_y / leg + Y
        return x, y
    
    pygame.draw.line(surface, stylus_color, [X, Y], trend(pygame.mouse.get_pos()), width_stylus)
       
       
       
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


def gameloop():
    
    pygame.init()

    dis = pygame.display.set_mode((WIDTH, HEIGHT))
    
    shift_x = 0
    shift_y = 0
    
    up, down, left, right = False, False, False, False
    
    stylus = 20
    fire = False
    count = 1
    
    play = True
    
    while play:
        count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        
        dis.fill(BLACK)
        draw_character(surface=dis, color_hair=RED, color_body=GRAY)
        draw_stylus(surface=dis, stylus_color=GRANDIS, width_stylus=4)        
        pygame.display.update()
        
    pygame.quit()
    
    quit()
    
gameloop()