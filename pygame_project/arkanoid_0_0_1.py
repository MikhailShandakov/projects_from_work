import pygame


WIDTH = 800
HEIGHT = 600
LINE = 40  # делим экран на условные линии
FPS = 60


WHITE = (250, 250, 250)
BLACK = (5, 5, 5)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
GREY = (50, 50, 50)


bord_lenght = 50
bord_start_position = WIDTH / 2
bord_speed = 10
bord_start = True

pygame.init()

dis = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


STEP = int(HEIGHT / LINE)
POSITION = bord_start_position
MOVE = 0


play = True
while play:
    
    
    LEFT_SIDE = POSITION - bord_lenght
    RIGHT_SIDE = POSITION + bord_lenght
    POSITION += MOVE
    
    if bord_start:
        X_CIRCLE = POSITION
        Y_CIRCLE = STEP * (LINE - 4)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MOVE = -bord_speed
            elif event.key == pygame.K_RIGHT:
                MOVE = bord_speed
            if event.key == pygame.K_SPACE and bord_start == True:
                bord_start = False
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and MOVE <= bord_speed:
                MOVE = 0
                
            elif event.key == pygame.K_RIGHT and MOVE >= bord_speed:
                MOVE = 0
                
    if POSITION < bord_lenght:
        POSITION = bord_lenght
        MOVE = 0
    
    elif POSITION > WIDTH - bord_lenght:
        POSITION = WIDTH - bord_lenght
        MOVE = 0
        
    if bord_start == False:
        x_change = 1
        y_change = 1
        
            
                
    clock.tick(FPS) 
    dis.fill(BLACK)
    pygame.draw.line(dis, GREY, [WIDTH * 0, STEP * 1], [WIDTH * 1, STEP * 1], STEP)  # Верхняя линия
    pygame.draw.line(dis, GREY, [WIDTH * 0, STEP * (LINE - 1)], [WIDTH * 1, STEP * (LINE - 1)], STEP)  # Нижняя линия
    pygame.draw.line(dis, WHITE, [LEFT_SIDE, STEP * (LINE - 3)], [RIGHT_SIDE, STEP * (LINE - 3)], STEP)  # Арканоид
    pygame.draw.circle(dis, WHITE, [X_CIRCLE, Y_CIRCLE], STEP / 2)
    pygame.display.update()
    
pygame.quit()

quit()