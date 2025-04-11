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
x_mouse = -1
y_mouse = -1
chek_point_x = "int"
chek_point_y = "int"
pygame.draw.rect(dis, BLACK, [world_position_x, world_position_y, world_width, world_height])

pygame.display.update()

while play:

    
    x1 = int(WIDTH / 2) - int(WIDTH / 2) % PIXEL
    y1 = int(HEIGHT / 2) - int(HEIGHT / 2) % PIXEL
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
                
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                
                shift_to_the_left, shift_to_the_right = "OFF", "OFF"
                shift_to_the_up, shift_to_the_down = "OFF", "OFF"
                
                x_mouse, y_mouse = e.pos
                x_mouse = x_mouse - x_mouse % PIXEL
                y_mouse = y_mouse - y_mouse % PIXEL
                
                if x1 < x_mouse:
                    shift_to_the_left = "ON"
                elif x1 > x_mouse:
                    shift_to_the_right = "ON"
                    
                if y1 < y_mouse:
                    shift_to_the_up = "ON"
                elif y1 > y_mouse:
                    shift_to_the_down = "ON"
                    
                chek_point_x = world_position_x + x1 - x_mouse
                chek_point_y = world_position_y + y1 - y_mouse
                    
    if world_position_x == chek_point_x:
        shift_to_the_right = "OFF"
        shift_to_the_left = "OFF"
        
    if world_position_y == chek_point_y:
        shift_to_the_up = "OFF"
        shift_to_the_down = "OFF"
        
        
            
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
# НЕ РАБОТАЕТ:            
#     def draw_object(x_object, y_object, width_object, height_object):
#         global world_position_x
#         global world_position_y
#         x_object += world_position_x
#         y_object += world_position_y
#         if ((x1 - width_object_1) < x_object_1 < (x1 + width) and
#             (y1 - height_object_1) < y_object_1 < (y1 + height)):
#                 world_position_x = past_position_x
#                 world_position_y = past_position_y
#         pygame.draw.rect(dis, WHITE, [x_object, y_object, width_object, height_object])
#      draw_object(1300, 1300, PIXEL * 10, PIXEL * 6)
        
        
    object_1 = 1500
    x_object_1 = world_position_x + object_1
    y_object_1 = world_position_y + object_1
    width_object_1 = PIXEL * 10
    height_object_1 = PIXEL * 6
    if (x1 - width_object_1) < x_object_1 < (x1 + width):
        if (y1 - height_object_1) < y_object_1 < (y1 + height):
            world_position_x = past_position_x
            world_position_y = past_position_y
            
    
    dis.fill(WHITE)
    
    pygame.draw.rect(dis, BLACK, [world_position_x, world_position_y, world_width, world_height])
    
    pygame.draw.rect(dis, WHITE, [x_object_1, y_object_1, width_object_1, height_object_1])
    
    pygame.draw.rect(dis, ORANGE, [x1, y1, width, height])
    
    pygame.display.update()
    
pygame.quit()

quit()
        
                