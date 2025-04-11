import pygame

FPS = 10

RED = 0
GREEN = 0
BLUE = 0


pygame.init()

dis = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

red_flag = "STOP"
green_flag = "STOP"
blue_flag = "STOP"

play = True

while play:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                red_flag = "UP"
            elif event.key == pygame.K_w:
                green_flag = "UP"
            elif event.key == pygame.K_e:
                blue_flag = "UP"
            elif event.key == pygame.K_a:
                red_flag = "DOWN"
            elif event.key == pygame.K_s:
                green_flag = "DOWN"
            elif event.key == pygame.K_d:
                blue_flag = "DOWN"
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                red_flag = "STOP"
            elif event.key == pygame.K_w:
                green_flag = "STOP"
            elif event.key == pygame.K_e:
                blue_flag = "STOP"
            elif event.key == pygame.K_a:
                red_flag = "STOP"
            elif event.key == pygame.K_s:
                green_flag = "STOP"
            elif event.key == pygame.K_d:
                blue_flag = "STOP"
                
    if red_flag == "UP" and RED < 255:
        RED += 1
    elif red_flag == "DOWN" and RED > 0:
        RED -= 1
        
    if green_flag == "UP" and GREEN < 255:
        GREEN += 1
    elif green_flag == "DOWN" and GREEN > 0:
        GREEN -= 1
        
    if blue_flag == "UP" and BLUE < 255:
        BLUE += 1
    elif blue_flag == "DOWN" and BLUE > 0:
        BLUE -= 1
    
    dis.fill((RED, GREEN, BLUE))
    
    pygame.display.set_caption(f"| Красный:{RED} | Зеленый:{GREEN} | Синий:{BLUE} |")
    
    pygame.display.update()
    
pygame.quit()

quit()