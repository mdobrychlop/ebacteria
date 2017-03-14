from pygame.locals import *
import math
import pygame
import random
import sys


class BactSprite(pygame.sprite.Sprite):

    def __init__(self, position, direction, src_image, multiplier):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(src_image)
        self.position = position
        self.direction = direction
        self.speed = 0
        self.multiplier = multiplier

    def motility(self, windowsize, ticks):
        """
        Controls all aspects of the cell's movement.
        """

        switch_span = 10 * self.multiplier  # ctrls freq of movement changes
        max_speed = 10 * self.multiplier
        min_speed = 0
        turn_angle = 40  # max angle of a single turn
        bounce_speed = 5 * self.multiplier  # window border bounce speed
        bounce_margin = 50  # window border width

        # higher switch_span -> lower freq of movement changes
        if ticks % switch_span == 0:
            # draw random speed and turn angle values
            rand_speed = random.randrange(min_speed, max_speed)
            self.speed = (rand_speed)
            rand_direction = random.randrange(-turn_angle, turn_angle)
            self.direction += (rand_direction)

            # bounce back if you're too close to the window's border
            # bounce them towards the middle of the screen, but not
            # at a right angle - looks weird with many cells displayed
            if self.position[0] >= windowsize[0] - bounce_margin:
                self.direction = random.randrange(80, 100)
                self.speed = (bounce_speed)
            if self.position[1] >= windowsize[1] - bounce_margin:
                self.direction = random.randrange(-10, 10)
                self.speed = (bounce_speed)
            if self.position[0] <= bounce_margin:
                self.direction = random.randrange(-100, -80)
                self.speed = (bounce_speed)
            if self.position[1] <= bounce_margin:
                self.direction = random.randrange(170, 190)
                self.speed = (bounce_speed)

    def update(self, deltat):
        """
        Updates the cell's position and orientation.
        """
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

winx = 800
winy = 600
windowsize = (winx, winy)
window = pygame.display.set_mode(windowsize)

number_of_bacteria = 15

bacteria = []

for i in range(number_of_bacteria):
    draw_coord = (random.randrange(50, winx-50),
                  random.randrange(50, winy-50))
    draw_direction = random.randrange(-180, 180)

    # multiplier is a float that has to be truncated to 1 digit after the dot
    # otherwise the game freezes right after generating initial positions
    multipl = random.uniform(0.1, 1.5)
    multipl = float(str(multipl)[:3])
    print(multipl)
    bact = BactSprite(draw_coord, draw_direction, 'black_test3.png', multipl)
    bacteria.append(bact)

bact_group = pygame.sprite.RenderPlain(bacteria)
clock = pygame.time.Clock()

while 1:
    deltat = clock.tick(60)

    for bact in bacteria:
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
