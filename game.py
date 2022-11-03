import pygame
import time
import sys

pygame.init()

screen = pygame.display.set_mode((400,400))

while True:
    #1 check for user input (key press, mouse clicks, etc!)
    print("------- CHECKING --------")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            print("YOU MOVED THE MOUSE!!")
        if event.type == pygame.QUIT:
            sys.exit()
        #if event.type == pygame.KEYUP:
            #screen.fill
    print("------- DONE CHECKING --------")

    pygame.display.flip()
    time.sleep(1)