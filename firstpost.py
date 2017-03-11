import pygame
import sys
import math
from pygame.locals import *


class BactSprite(pygame.sprite.Sprite):

    def __init__(self, position):
        # not sure why this is here, will ask somewhere and let you know
        pygame.sprite.Sprite.__init__(self)
        # basic.png is the bacterium image from the previous example
        self.src_image = pygame.image.load('basic.png')
        self.position = position

    def update(self):
        # this method will be expanded to add movement
        self.image = self.src_image
        self.rect = self.image.get_rect()
        self.rect.center = self.position

# display a 800x600 window
window = pygame.display.set_mode((800, 600))
# get the middle of the window so we can place the bacterium there
rect = window.get_rect()

# create the bacterium object and draw it
bact = BactSprite(rect.center)
bact_group = pygame.sprite.RenderPlain(bact)

# main game loop
while 1:
    # checking if there's some input from the player
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        # close the game when ESC is pressed
        if event.type == pygame.QUIT or event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    # after checking the events, clear the window...
    window.fill((0, 0, 0))

    # and redraw the bacterium's sprite
    bact_group.update()
    bact_group.draw(window)
    pygame.display.flip()
