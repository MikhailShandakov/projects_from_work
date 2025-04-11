import pygame

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (5, 5, 230)
GREY = (225, 225, 225)
PINK = (230, 50, 230)
YELLOW = (220, 230 ,0)

pygame.init()

dis = pygame.display.set_mode((800, 600))


dis.fill(BLUE)

polygon = pygame.draw.polygon(dis, WHITE, [[100.5, 70], [630, 110], [700, 220], [70, 200], [400, 150]])
line = pygame.draw.aalines(dis, WHITE, True, [[100, 70], [630, 110], [700, 220], [70, 200], [400, 150]])
pygame.display.update()

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
            
pygame.quit()

quit()

clock = pygame.time.Clock()