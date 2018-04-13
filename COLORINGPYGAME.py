import sys
#imports pygame
import pygame
#imports random
import random
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

#set pi
PI = 3.141592653
#set screen size - display.set_mode(size)
size = (600, 400)
screen = pygame.display.set_mode(size)
#window title
pygame.display.set_caption("RAINBOW COLOR")
#game loop
done = False
#getting clock function from pygame Clock is a function inside class time
clock = pygame.time.Clock()
#Loop done is not so it runs
screen.fill(BLACK)
#color changer
r = 250
g = 0
b = 0
RB = rainbow(r,g,b)

while not done: 
    #References screen variable, pygame.display.set_mode.fill(WHITE)
    #fills screen white Drawing codes go below this
    #main event loop inputs and such
    pygame.draw.rect(screen, (r,g,b), (0,0,20,400), 0)
    a = pygame.mouse.get_pos()
    for event in pygame.event.get(): #Searches for user input
        
        if event.type == pygame.QUIT: # if user clicks close in scan for user input
            done = True #Done is set to True loop ends
            pygame.quit()
        #get pressed tells us if a mouse is pressed or not if the 0 position of
        #get_pressed is true or set to 1 then the following will run
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(BLACK)
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, (r,g,b), (a[0],a[1]), 12, 0)
            
        if pygame.mouse.get_pressed()[0]:
            r = RB.red_func()
            g = RB.green_func()
            b = RB.blue_func()
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                r = RB.red_func_change()
                g = RB.green_func_change()
                b = RB.blue_func_change()
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                r = 0
                g = 0
                b = 0
            




    
    #Updates screen
    pygame.display.flip()
    #Sets refresh rate references clock pygametime.Clock()
    clock.tick(200)
    
    
