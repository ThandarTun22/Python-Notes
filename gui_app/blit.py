
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300),0,32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
catImage = pygame.image.load('flappy_bird.png')
imageX = 10
imageY = 10
direction = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        imageX += 5
        if imageX == 280:
            direction == 'down'
    elif direction == 'down':
        imageY += 5
        if imageY == 220:
            direction = 'left'
    elif direction == 'left':
        imageX -= 5
        if imageX == 10:
            direction = 'up'
    elif direction == 'up':
        imageY -= 5
        if imageY == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImage, (imageX, imageY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
