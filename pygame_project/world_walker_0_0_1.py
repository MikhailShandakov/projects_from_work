import pygame

FPS = 60

WHITE = (230, 230, 230)
BLACK = (30, 30, 30)
ORANGE = (230, 150, 0)
RED = (230, 0, 0)
GREEN = (0, 230, 0)

WIDTH = 800
HEIGHT = 600

PIXEL = 2

pygame.init()

dis = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

shift_to_the_right = "OFF"
shift_to_the_left = "OFF"
shift_to_the_up = "OFF"
shift_to_the_down = "OFF"
boost = "OFF"
play = True

boost_count = 0


world_position_x = -1000
world_position_y = -1000
world_width = 3000
world_height = 2000
pygame.draw.rect(dis, BLACK, [world_position_x, world_position_y, world_width, world_height])

pygame.display.update()

while play:
    
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    width = PIXEL * 10
    height = PIXEL * 12
    past_position_x = world_position_x
    past_position_y = world_position_y
    
    clock.tick(FPS)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            play = False
        
        if e.type == pygame.KEYDOWN:
            
            if e.key == pygame.K_RIGHT:
                shift_to_the_left = "ON"
            elif e.key == pygame.K_LEFT:
                shift_to_the_right = "ON"
            elif e.key == pygame.K_UP:
                shift_to_the_down = "ON"
            elif e.key == pygame.K_DOWN:
                shift_to_the_up = "ON"
            elif e.key == pygame.K_SPACE:
                boost == "ON"
                
        if e.type == pygame.KEYUP:
            
            if e.key == pygame.K_RIGHT:
                shift_to_the_left = "OFF"
            elif e.key == pygame.K_LEFT:
                shift_to_the_right = "OFF"
            elif e.key == pygame.K_UP:
                shift_to_the_down = "OFF"
            elif e.key == pygame.K_DOWN:
                shift_to_the_up = "OFF"
            
    if shift_to_the_left == "ON":
        past_position_x = world_position_x
        world_position_x -= PIXEL
        if boost == "ON" and boost_count == 0:
            world_position_x -= PIXEL
            
    if shift_to_the_right == "ON":
        past_position_x = world_position_x
        world_position_x += PIXEL
        if boost == "ON" and boost_count == 0:
            world_position_x += PIXEL
            
    if shift_to_the_up == "ON":
        past_position_y = world_position_y
        world_position_y -= PIXEL
        if boost == "ON" and boost_count == 0:
            world_position_y -= PIXEL
            
    if shift_to_the_down == "ON":
        past_position_y = world_position_y
        world_position_y += PIXEL
        if boost == "ON" and boost_count == 0:
            world_position_x += PIXEL
            
    object_1 = 1300
    x_object_1 = world_position_x + object_1
    y_object_1 = world_position_y + object_1
    width_object_1 = PIXEL * 10
    height_object_1 = PIXEL * 6
    if (x1 - width_object_1) < x_object_1 < (x1 + width):
        if (y1 - height_object_1) < y_object_1 < (y1 + height):
#             shift_to_the_right = "OFF"
#             shift_to_the_left = "OFF"
#             shift_to_the_up = "OFF"
#             shift_to_the_down = "OFF"
            world_position_x = past_position_x
            world_position_y = past_position_y
            
    
    dis.fill(WHITE)
    
    pygame.draw.rect(dis, BLACK, [world_position_x, world_position_y, world_width, world_height])
    
    pygame.draw.rect(dis, WHITE, [x_object_1, y_object_1, width_object_1, height_object_1])
    
    pygame.draw.rect(dis, ORANGE, [x1, y1, width, height])
    
    pygame.display.update()
    
pygame.quit()

quit()
        
                