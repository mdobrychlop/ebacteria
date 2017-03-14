from pygame.locals import *
import math
import pygame
import random
import sys


class BactSprite(pygame.sprite.Sprite):

    def __init__(self, position, src_image):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(src_image)
        self.position = position
        self.direction = 0
        self.speed = 0

    def motility(self, windowsize, ticks):
        switch_freq = 10
        max_speed = 10
        min_speed = 0
        turn_angle = 40
        bounce_speed = 5
        bounce_margin = 50

        if ticks % switch_freq == 0:
            rand_speed = random.randrange(min_speed, max_speed)
            self.speed = (rand_speed)
            rand_direction = random.randrange(-turn_angle, turn_angle)
            self.direction += (rand_direction)

            if self.position[0] >= windowsize[0] - bounce_margin:
                self.direction = 90
                self.speed = (bounce_speed)
            if self.position[1] >= windowsize[1] - bounce_margin:
                self.direction = 0
                self.speed = (bounce_speed)
            if self.position[0] <= bounce_margin:
                self.direction = -90
                self.speed = (bounce_speed)
            if self.position[1] <= bounce_margin:
                self.direction = 180
                self.speed = (bounce_speed)

    def update(self, deltat):
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

winx = 800
winy = 600
windowsize = (winx, winy)
window = pygame.display.set_mode(windowsize)

draw_coord = (random.randrange(100, winx-100), random.randrange(100, winy-100))

bact = BactSprite(draw_coord, 'black_test3.png')
bact_group = pygame.sprite.RenderPlain(bact)
clock = pygame.time.Clock()

while 1:
    deltat = clock.tick(60)

    bact.motility(windowsize, pygame.time.get_ticks())

    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        if event.type == pygame.QUIT or event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    window.fill((150, 150, 150))
    bact_group.update(deltat)
    bact_group.draw(window)
    pygame.display.flip()
