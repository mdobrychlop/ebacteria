import pygame
import sys
import math
from pygame.locals import *


class BactSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load('basic.png')
        self.position = position
        self.direction = 0
        self.speed = 0
        self.k_left = 0
        self.k_right = 0
        self.k_up = 0
        self.k_down = 0

    def update(self, deltat):
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


window = pygame.display.set_mode((640, 480))
rect = window.get_rect()
bact = BactSprite(rect.center)
bact_group = pygame.sprite.RenderPlain(bact)
clock = pygame.time.Clock()

while 1:
    deltat = clock.tick(60)
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue

        down = event.type == KEYDOWN
        if event.key == K_RIGHT:
            bact.k_right = down * -5
        if event.key == K_LEFT:
            bact.k_left = down * 5
        if event.key == K_UP:
            bact.k_up = down * 2
        if event.key == K_DOWN:
            bact.k_down = down * -2
        if event.type == pygame.QUIT or event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    bact_group.update(deltat)
    bact_group.draw(window)
    pygame.display.flip()
