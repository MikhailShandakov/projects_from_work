import pygame

FPS = 60

BLACK = (20, 20, 20)
GREY = (140, 140, 140)
DARK_GREY = (85, 85, 85)
LIGHT_GREY = (210, 210, 210)
DARK = (60, 60, 60)

Zx = 1 / 4
Zy = 1 / 8

pygame.init()

dis = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()

world_position_x = -1000
world_position_y = 500
world_lenght = 3000
world_height = 100
world_width = 2000

player_position_x = 400
player_position_y = 300
player_width = 10

shift_to_the_right = "OFF"
shift_to_the_left = "OFF"
shift_to_the_up = "OFF"
shift_to_the_down = "OFF"
play = True

while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                shift_to_the_left = "ON"
            if event.key == pygame.K_LEFT:
                shift_to_the_right = "ON"
            if event.key == pygame.K_UP:
                shift_to_the_down = "ON"
            if event.key == pygame.K_DOWN:
                shift_to_the_up = "ON"
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                shift_to_the_left = "OFF"
            if event.key == pygame.K_LEFT:
                shift_to_the_right = "OFF"
            if event.key == pygame.K_UP:
                shift_to_the_down = "OFF"
            if event.key == pygame.K_DOWN:
                shift_to_the_up = "OFF"
                
                
    if shift_to_the_left == "ON":
        world_position_x -= 1
    if shift_to_the_right == "ON":
        world_position_x += 1
    if shift_to_the_up == "ON":
        world_position_y -= 1
    if shift_to_the_down == "ON":
        world_position_y += 1
        
    dis.fill(LIGHT_GREY)
    
    Zx_world = Zx * world_width + world_position_x
    Zy_world = Zy * world_width + world_position_y
    pygame.draw.rect(dis, GREY, [world_position_x, world_position_y, world_lenght, world_height])
    pygame.draw.rect(dis, GREY, [Zx_world, Zy_world, world_lenght, world_height])
    pygame.draw.aaline(dis, GREY, (world_position_x, world_position_y), (Zx_world, Zy_world))
    pygame.draw.aaline(dis, GREY, (world_position_x + world_lenght, world_position_y), (Zx_world + world_lenght, Zy_world))
    pygame.draw.aaline(dis, GREY, (world_position_x, world_position_y + world_height), (Zx_world, Zy_world + world_height))
    pygame.draw.aaline(dis, GREY, (world_position_x + world_lenght, world_position_y + world_height), (Zx_world + world_lenght, Zy_world + world_height))
    
    pygame.display.update()
        
pygame.quit()

quit()
    
                
                
    
