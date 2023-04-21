
import pygame , sys
from pygame.locals import *

pygame.init()

DISPLAYSURF =   pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Drawing')

WHITE = (255,0,0)  # RGB value 0 - 255 # tuple value
# draw on the surface object

DISPLAYSURF.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()