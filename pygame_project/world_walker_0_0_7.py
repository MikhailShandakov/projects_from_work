import pygame

FPS = 60

WHITE = (230, 230, 230)
BLACK = (35, 35, 29)
ORANGE = (230, 150, 0)
RED = (230, 0, 0)
GREEN = (0, 86, 26)
LIGHT_GREEN = (0, 90, 30)
GREY = (65, 70, 60)
BLUE = (30, 100, 255)
LIGHT_BLUE = (70, 140, 90)

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
x_mouse = WIDTH / 2
y_mouse = HEIGHT / 2
chek_point_x = "OFF"
chek_point_y = "OFF"
speed_x = 1
speed_y = 1

object_list = [[1500, 1500, 12, 10], [1500, 1300, 3, 20], [1234, 1323, 30, 30]]
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
            
            shift_to_the_left, shift_to_the_right = "OFF", "OFF"
            shift_to_the_up, shift_to_the_down = "OFF", "OFF"
            
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
                
            chek_point_x = "OFF"
            chek_point_y = "OFF"
                
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
                
                different_x = x1 - x_mouse
                different_y = y1 - y_mouse
                
                if abs(different_x) < PIXEL * speed_x:
                    speed_x = 2
                if abs(different_y) < PIXEL * speed_y:
                    speed_y = 2
                
                if x1 < x_mouse:
                    shift_to_the_left = "ON"
                elif x1 > x_mouse:
                    shift_to_the_right = "ON"
                    
                if y1 < y_mouse:
                    shift_to_the_up = "ON"
                elif y1 > y_mouse:
                    shift_to_the_down = "ON"
                    
                chek_point_x = world_position_x + different_x
                chek_point_y = world_position_y + different_y
                    
    if world_position_x == chek_point_x:
        shift_to_the_right = "OFF"
        shift_to_the_left = "OFF"
        speed_x = 1
        
    if world_position_y == chek_point_y:
        shift_to_the_up = "OFF"
        shift_to_the_down = "OFF"
        speed_y = 1
        
        
    if abs(x1 - x_mouse) < PIXEL * speed_x:
        speed_x = 1
    if abs(y1 - y_mouse) < PIXEL * speed_y:
        speed_y = 1
    
    if shift_to_the_left == "ON":
        past_position_x = world_position_x
        world_position_x -= PIXEL * speed_x
        if boost == "ON" and boost_count == 0:
            world_position_x -= PIXEL
            
    if shift_to_the_right == "ON":
        past_position_x = world_position_x
        world_position_x += PIXEL * speed_x
        if boost == "ON" and boost_count == 0:
            world_position_x += PIXEL
            
    if shift_to_the_up == "ON":
        past_position_y = world_position_y
        world_position_y -= PIXEL * speed_y
        if boost == "ON" and boost_count == 0:
            world_position_y -= PIXEL
            
    if shift_to_the_down == "ON":
        past_position_y = world_position_y
        world_position_y += PIXEL * speed_y
        if boost == "ON" and boost_count == 0:
            world_position_x += PIXEL
        
    for obj in object_list:
        x_object = obj[0] + world_position_x
        y_object = obj[1] + world_position_y
        width_object = obj[2] * PIXEL
        height_object = obj[3] * PIXEL
        
        if x1 - width_object < x_object < x1 + width:
            if y1 - height_object < y_object < y1 + height:
                world_position_x = past_position_x
                world_position_y = past_position_y
    
    dis.fill(BLACK)
    
    pygame.draw.rect(dis, GREEN, [world_position_x, world_position_y, world_width, world_height])
    
    for i in range(0, world_width, 33):
        for j in range(0, world_height, 20):
            if i % 2 == 0:
                j += 10
            pygame.draw.rect(dis, LIGHT_GREEN, [j + world_position_x, i + world_position_y, 10, 12])
    
    for obj in object_list:
        x_object = obj[0] + world_position_x
        y_object = obj[1] + world_position_y
        width_object = obj[2] * PIXEL
        height_object = obj[3] * PIXEL
        
        pygame.draw.rect(dis, GREY, [x_object, y_object, width_object, height_object])
    
    pygame.draw.rect(dis, LIGHT_BLUE, [x1, y1, width, height])
    pygame.draw.circle(dis, BLUE, [x1 + width / 2, y1 + height / 2], 5)
    
    pygame.display.update()
    
pygame.quit()

quit()
        
                