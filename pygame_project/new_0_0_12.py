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

SHIFT_UP, SHIFT_DOWN, SHIFT_LEFT, SHIFT_RIGHT = HEIGHT / 2, HEIGHT / 2, WIDTH / 2, WIDTH / 2


def gameloop():
    
    pygame.init()

    dis = pygame.display.set_mode((WIDTH, HEIGHT))
    
    reverse_character = False
    
    shift_x = 0
    shift_y = 0
    
    up, down, left, right = False, False, False, False
    
    stylus = 20
    
    count_up, count_down, count_left, count_right = HEIGHT / 2, HEIGHT / 2, WIDTH / 2, WIDTH / 2
            
    bullet_dict = {}
    tree_dict = {"start_loc1": [random.randrange(WIDTH), random.randrange(HEIGHT // 2 - 50)],
                 "start_loc2": [random.randrange(WIDTH), random.randrange(HEIGHT // 2 + 50, HEIGHT)],
                 "start_loc3": [random.randrange(WIDTH // 2 + 50, WIDTH), random.randrange(HEIGHT)],
                 "start_loc4": [random.randrange(WIDTH // 2 - 50), random.randrange(HEIGHT)]}
    
    def get_step(mouse_x, mouse_y):
        x = abs(X - mouse_x)
        y = abs(Y - mouse_y)
        b = (x ** 2 + y ** 2) ** 0.5
        p_1 = stylus * x / b
        p_2 = stylus * y / b
        
        return p_1, p_2
    
    def tree(dict2):
        for tree_x, tree_y in dict2.values():
            pygame.draw.rect(dis, BROWN, [tree_x, tree_y, 10, 40])
            pygame.draw.circle(dis, GREEN, [tree_x + 5, tree_y], 20)
    
    def character(rev):
        if rev:
            pygame.draw.circle(dis, RED, [X - 2, Y - 10], 10)
            pygame.draw.circle(dis, RED, [X - 12, Y - 10], 4)
            pygame.draw.rect(dis, GRAY, [X - 8, Y - 10, 16, 20])
            pygame.draw.line(dis, BLACK, [X + 4, Y - 6], [X + 1, Y - 6])
            pygame.draw.line(dis, BLACK, [X - 12, Y - 14], [X - 12, Y - 10])
        else:
            pygame.draw.circle(dis, RED, [X + 2, Y - 10], 10)
            pygame.draw.circle(dis, RED, [X + 12, Y - 10], 4)
            pygame.draw.rect(dis, GRAY, [X - 8, Y - 10, 16, 20])
            pygame.draw.line(dis, BLACK, [X - 4, Y - 6], [X - 1, Y - 6])
            pygame.draw.line(dis, BLACK, [X + 12, Y - 14], [X + 12, Y - 10])
            
    def bullet(dict1):
        for bul_x, bul_y in dict1.values():
            pygame.draw.circle(dis, WHITE, [bul_x, bul_y], 4)
    
    fire = False
    
    count = 1
    play = True

    while play:
        count += 1
        shift_up = up / 2
        shift_down = down / 2
        shift_left = left / 2
        shift_right = right / 2
        
        pos = pygame.mouse.get_pos()
        
        step_x, step_y = get_step(pos[0], pos[1])
        
        if pos[0] > WIDTH / 2:
            reverse_character = True
            stylus_x = X + step_x
        else:
            reverse_character = False
            step_x *= -1
            stylus_x = X + step_x
            
        if pos[1] > HEIGHT / 2:
            stylus_y = Y + step_y
        else:
            step_y *= -1
            stylus_y = Y + step_y
        
        count_up += shift_up
        count_down += shift_down
        count_left += shift_left
        count_right += shift_right
        
        copy_dict = bullet_dict.copy()
        for i in copy_dict:
            new_x = copy_dict[i][0] + i[0] / 10 + shift_left - shift_right
            new_y = copy_dict[i][1] + i[1] / 10 + shift_up - shift_down
            
            bullet_dict[i] = [new_x, new_y]
            
            if not 0 < new_x < WIDTH or not 0 < new_y < HEIGHT:
                del bullet_dict[i]
                continue
            pass
        
        copy_dict = tree_dict.copy()
        for i in copy_dict:
            new_x = tree_dict[i][0] + shift_left - shift_right
            new_y = tree_dict[i][1] + shift_up - shift_down
            
            tree_dict[i] = [new_x, new_y]
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                

                
            elif event.type == pygame.KEYDOWN:
#                 if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
#                     up, down, left, right = False, False, False, False
                    
                if event.key == pygame.K_w:
                    up = True
                elif event.key == pygame.K_s:
                    down = True
                elif event.key == pygame.K_a:
                    left = True
                elif event.key == pygame.K_d:
                    right = True
                    
            elif event.type == pygame.KEYUP:
                
                if event.key == pygame.K_w:
                    up = False
                elif event.key == pygame.K_s:
                    down = False
                elif event.key == pygame.K_a:
                    left = False
                elif event.key == pygame.K_d:
                    right = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    fire = count
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    fire = False
        
        
        key_x, key_y = count_up - count_down, count_right - count_left
        
        if key_y > SHIFT_UP:
            tree_dict.setdefault((key_x // SHIFT_UP, key_y // SHIFT_UP), [random.randrange(WIDTH), random.randrange(-SHIFT_UP, 0)])
            
        if key_y < -SHIFT_DOWN:
            tree_dict.setdefault((key_x // SHIFT_UP, key_y // SHIFT_DOWN), [random.randrange(WIDTH), random.randrange(HEIGHT, HEIGHT + SHIFT_UP)])
            
        if key_x < -SHIFT_LEFT:
            tree_dict.setdefault((key_x // SHIFT_LEFT, key_y // SHIFT_LEFT), [random.randrange(-SHIFT_LEFT, 0), random.randrange(HEIGHT)])
            
        if key_x > SHIFT_RIGHT:
            tree_dict.setdefault((key_x // SHIFT_RIGHT, key_y // SHIFT_RIGHT), [random.randrange(WIDTH, WIDTH + SHIFT_RIGHT), random.randrange(HEIGHT)])
            

        if fire == count or (fire and (count - fire) % 60 == 0):
            bullet_dict[(step_x, step_y, count)] = [stylus_x, stylus_y]
        

        dis.fill(BLACK)
        tree(tree_dict)
        character(reverse_character)
        pygame.draw.line(dis, GRANDIS, [X, Y], [stylus_x, stylus_y], 4)
        pygame.draw.circle(dis, GRAY, [X, Y], 4)
        bullet(bullet_dict)
        pygame.display.update()
            
    pygame.quit()
    
    quit()


gameloop()