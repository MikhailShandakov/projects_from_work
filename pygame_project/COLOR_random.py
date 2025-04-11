import pygame
import random

FPS = 30
DELAY = 10

COUNT = 1000

pygame.init()

dis = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()

s = []

speed_flag = "NORMAL"
stop_flag = "GO"
play = True

while play:
    
    clock.tick(FPS)
    
    print(DELAY)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_flag = "RAISE"
            elif event.key == pygame.K_DOWN:
                speed_flag = "PASS"
            
            if event.key == pygame.K_SPACE:
                if stop_flag == "GO":
                    stop_flag = "STOP"
                else:
                    stop_flag = "GO"
                    
            if event.key == pygame.K_p:
                print(f"| Красный:{RED} | Зеленый:{GREEN} | Синий:{BLUE} |")
                s.append((RED, GREEN, BLUE))
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed_flag = "NORMAL"
            elif event.key == pygame.K_DOWN:
                speed_flag = "NORMAL"
        
            
    if speed_flag == "RAISE" and DELAY < 30:
        DELAY += 1
    elif speed_flag == "PASS" and DELAY > 1:
        DELAY -= 1
        
    if stop_flag == "GO":
        COUNT += DELAY
        
    if stop_flag == "GO" and COUNT >= 1000:
        COUNT = 0
        RED = random.randrange(0, 256)
        GREEN = random.randrange(0, 256)
        BLUE = random.randrange(0, 256)
    
    dis.fill((RED, GREEN, BLUE))
    
    pygame.display.set_caption(f"| Красный:{RED} | Зеленый:{GREEN} | Синий:{BLUE} |")
    
    pygame.display.update()
        
print(s)

pygame.quit()

quit()