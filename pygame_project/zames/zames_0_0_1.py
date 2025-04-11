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


def stylus_get_position(mouse_position: tuple, lenght_stylus=20):
    mouse_x, mouse_y = map(lambda mouse, center: abs(center - mouse), mouse_position, [X, Y])
    leg = (mouse_x ** 2 + mouse_y ** 2) ** 0.5
    x = lenght_stylus * mouse_x / leg
    y = lenght_stylus * mouse_y / leg
    return x, y


def gameloop():
    pass

gameloop()