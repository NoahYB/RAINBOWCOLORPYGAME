
#imports pygame
import pygame
#import the class i made for rainbow color
from classes import rainbow
#starts pygame module
pygame.init()
#determine colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
#set screen size - display.set_mode(size)
size = (600, 400)
screen = pygame.display.set_mode(size)
#window title
pygame.display.set_caption("RAINBOW COLOR")
#game loop
done = False
clock = pygame.time.Clock()
screen.fill(BLACK)
#INIT COLOR r,g,b
r = 240
g = 0
b = 0
RB = rainbow(r,g,b)
brush_size = 12
while not done: 
    pygame.draw.rect(screen, (r,g,b), (0,0,20,400), 0)
    a = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            #CLEARS SCREEN
            if event.key == pygame.K_SPACE:
                screen.fill(BLACK)
            #INCREASE BRUSH SIZE
            if event.key == pygame.K_UP:
                brush_size +=10
            #DECREASE BRUSH SIZE
            if event.key == pygame.K_DOWN:
                brush_size -=10
                if brush_size <0:
                    brush_size = 0
            if event.key == pygame.K_RIGHT:
                r = RB.red_func_change()
                g = RB.green_func_change()
                b = RB.blue_func_change()
            if event.key == pygame.K_p:
                pygame.image.save(screen, "screenshot.png")
        #DRAW
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, (r,g,b), (a[0],a[1]), brush_size, 0)
        #CHANGES COLORS
        if pygame.mouse.get_pressed()[0]:
            r = RB.red_func()
            g = RB.green_func()
            b = RB.blue_func()
        
            
    
    #CHANGES COLORS TO BLACK
    
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                r = 0
                g = 0
                b = 0
    
    




    
    #Updates screen
    pygame.display.flip()
    #Sets refresh rate references clock pygametime.Clock()
    clock.tick(60)
    
    
