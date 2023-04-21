import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF =   pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption("Drawing")

# set up the colors

BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

# DRAW ON THE SURFACE OBJECT
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146,0),(291,106),(236,277),(0,106)),3)
pygame.draw.line(DISPLAYSURF, BLUE, (60,60),(120,60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120,60),(60,120))
pygame.draw.line(DISPLAYSURF, BLUE, (60,120),(120,120),4)

pygame.draw.circle(DISPLAYSURF, RED, (300,50),20,0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300,250,40,80),1)
pygame.draw.rect(DISPLAYSURF, RED, (200,150,100,50))

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()