import pygame
import random
pygame.init()

FPS = 60

clock = pygame.time.Clock()

dis = pygame.display.set_mode((800, 300))

pygame.display.update()

speed_count = 0
move = "STOP"
x = random.randrange(0, 800)
y = 0
y_change = 0


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move = "GO"
                if speed_count < 0:
                    speed_count = 0
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move = "STOP"
                
    if move == "STOP":
        speed_count -= 1
        
    if move == "GO":
        speed_count += 1
        
    def speed(level):
        if level > 0:
            return round(level / 10)
        else:
            return 0
            
    y += speed(speed_count)
    
    if y > 300:
        y = 0
    
    dis.fill((255, 255, 255))
    
    pygame.draw.rect(dis, (255, 0, 0), [x, y, 10, 10])
    
    pygame.display.update()
    
    clock.tick(FPS)





pygame.quit()

quit()