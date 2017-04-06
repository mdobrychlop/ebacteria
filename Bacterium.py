from pygame.locals import *
import Drawing
import math
import pygame
import random
import sys


class Bacterium(pygame.sprite.Sprite):
    """
    Contains all the information concerning a single bacterium.
    """
    def __init__(self, position, direction, src_image,
                 multi, morph, size, color, id):

        pygame.sprite.Sprite.__init__(self)

        self.id = id
        self.size = size
        self.color = color
        self.highlight_color = (0, 255, 0)
        self.morph = morph
        self.highlighted = False
        self.position = position
        self.direction = direction
        self.speed = 0
        # original_speed stores speed before each pause
        self.original_speed = 0
        self.multiplier = multi
        self.transparency = self.random_transparency()

        if src_image == '':
            self.draw_from_shapes()
        else:
            self.draw_from_image(src_image)

    def draw_from_image(self, src_image):
        """
        Sets a provided image file as the cell's surface (main appearance).
        Slower, but potentially much prettier.
        """
        self.main_surface = pygame.image.load(src_image)

    def draw_from_shapes(self):
        """
        Defines a surface of a given size, and then draws the cell's shape
        on the surface using pygame's built-in shape drawing methods.
        Morphology defines what kind of shape the cell will display.
        More work to build the cell's appearance, but much better preformance.
        """
        self.width = self.size
        self.length = int(self.size*3.5)

        if self.highlighted is True:
            col = self.highlight_color
        else:
            col = self.color

        if self.morph == 'bacillus':
            # calculate the shapes needed to describe provided morphology
            cell_shape = Drawing.Bacillus(self.width, self.length, col)

        # set the main surface = background for the bacterium's shape
        self.main_surface = pygame.Surface((self.width, self.length))
        # set black pixels as transparent - to avoid default black outline
        self.main_surface.set_colorkey((0, 0, 0))

        # draw the shape on the surface
        cell_shape.draw_shape(self.main_surface, self.transparency)

    def random_transparency(self):
        r = random.randrange(1, 10)
        if r <= 2:
            random_alpha = random.randrange(120, 140)
        elif r <= 7:
            random_alpha = random.randrange(141, 160)
        else:
            random_alpha = random.randrange(161, 255)

        return random_alpha

    def motility(self, windowsize, ticks):
        """
        Controls all aspects of the cell's movement.
        PROBABLY REQUIRES MOVING TO ANOTHER CLASS ASAP.
        """

        switch_span = int(10 * self.multiplier)  # ~freq of movement changes
        max_speed = int(5 * self.multiplier)
        min_speed = 0
        turn_angle = 40  # max angle of a single turn
        bounce_speed = int(5 * self.multiplier)  # window border bounce speed
        bounce_margin = 50  # window border width

        # higher switch_span -> lower freq of movement changes
        if ticks % switch_span == 0:
            # draw random speed and turn angle values
            if max_speed == 0:
                max_speed = 1
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
        self.image = pygame.transform.rotate(self.main_surface, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
