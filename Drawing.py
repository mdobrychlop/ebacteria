from pygame import gfxdraw  # experimental, must be imported individually
import pygame
import random


class Bacillus():
    """
    A common, rod-like shape of bacteria.
    Here drawn as:
    - two circles (head and tail)
    - a rectangle (body) connecting head and tail
      ____________________
     /  |  \        /  |  \
    |   |   |      |   |   |
     \__|__/________\__|__/

     https://en.wikipedia.org/wiki/Bacillus_(shape)
    """
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.top_color = color
        self.border_width = self.calculate_border_width()

    def draw_shape(self, surface, transparency):
        """
        Draws the cell's shape on a given surface object.
        """
        # for now, the light grey contours are only modifiable here
        # the main cell color can be modified in the parameters
        bg_color = (200, 200, 200)
        mid_color = (175, 175, 175)
        top_color = self.top_color

        bg_contour_width = self.border_width
        mid_contour_width = self.border_width
        head_center = (int(self.width/2), int(self.width/2))
        tail_center = (int(self.width/2), int(self.length-self.width/2))

        # background / bottom layer
        bg_circle_radius = int(self.width/2) - 1
        bg_body_corners = self.calculate_body_corners(0)
        # middle layer
        mid_circle_radius = bg_circle_radius - bg_contour_width
        mid_body_corners = self.calculate_body_corners(bg_contour_width)
        # top layer
        top_circle_radius = bg_circle_radius - mid_contour_width*2
        top_body_corners = self.calculate_body_corners(mid_contour_width*2)

        # draw background layer
        self.draw_layer(surface, bg_circle_radius, head_center,
                        tail_center, bg_body_corners, bg_color)
        # draw middle layer
        self.draw_layer(surface, mid_circle_radius, head_center,
                        tail_center, mid_body_corners, mid_color)
        # draw top layer
        self.draw_layer(surface, top_circle_radius, head_center,
                        tail_center, top_body_corners, top_color)

        # add transparency
        surface.set_alpha(transparency)

    def calculate_body_corners(self, previous_layer_contour_width):
        """
        Calculates coordinates of the rectangular body's corners.
        """
        plcw = previous_layer_contour_width

        c1 = (plcw, int(self.width/2))
        c2 = (self.width-plcw, int(self.width/2))
        c3 = (self.width-plcw, int(self.length-self.width/2))
        c4 = (plcw, int(self.length-self.width/2))

        return (c1, c2, c3, c4)

    def calculate_border_width(self):
        """
        Makes sure the outline of the cell is not 0px wide.
        """
        border_width = int(self.width*0.2)
        if border_width == 0:
            border_width = 1

        return border_width

    def draw_layer(self, surface, circle_rad, head_center,
                   tail_center, body_corners, color, anti_aliasing=True):
        """
        Uses pygame's drawing methods to place shapes based on previously
        calculated coordinates and sizes.
        By default, the function uses experimental gfxdraw module
        instead of draw module, as gfxdraw generates smoother shapes.
        """
        # leaving this here just in case, but the aacircles look awful
        #
        # gfxdraw.aacircle(surface, head_center[0], head_center[1],
        #                 circle_rad, color)
        # gfxdraw.aacircle(surface, tail_center[0], tail_center[1],
        #                 circle_rad, color)
        #
        if anti_aliasing is True:
            # draw circular "head"
            gfxdraw.filled_circle(surface, head_center[0], head_center[1],
                                  circle_rad, color)
            # draw circular "tail"
            gfxdraw.filled_circle(surface, tail_center[0], tail_center[1],
                                  circle_rad, color)
            # draw rectangular "body"
            gfxdraw.filled_polygon(surface, body_corners, color)
        else:
            pygame.draw.circle(surface, color, head_center, circle_rad)
            pygame.draw.circle(surface, color, tail_center, circle_rad)
            pygame.draw.polygon(surface, color, body_corners)
