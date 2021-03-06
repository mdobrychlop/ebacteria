from pygame.locals import *
from pygame import gfxdraw
from Bacterium import Bacterium
from Events import EventControl
from Hud import InfoBox, ScreenText
import Config
import math
import pygame
import random
import sys


def generate_cells():
    """
    Generates bacteria objects for all bacteria.
    """
    bacteria = []
    identifier = 1
    for i in range(Config.NUMBER_OF_CELLS):
        draw_coord = (random.randrange(50, Config.WIN_X-50),
                      random.randrange(50, Config.WIN_Y-50))

        if Config.CELLS_NON_ROTATED is False:
            draw_direction = random.randrange(-180, 180)
        else:
            draw_direction = 0
        multipl = random.uniform(0.1, 1.5)
        # multiplier is a float that must be truncated to 1 digit after the dot
        # otherwise the game freezes right after generating initial positions
        multipl = float(str(multipl)[:3])
        bact = Bacterium(draw_coord, draw_direction, Config.PNG_IMAGE,
                         multipl, Config.MORPHOLOGY, Config.CELL_SIZE,
                         Config.CELL_COLOR, identifier)
        bacteria.append(bact)
        identifier += 1
    return bacteria


def main():
    infobox = InfoBox()
    screentext = ScreenText()
    bacteria = generate_cells()
    bact_group = pygame.sprite.RenderPlain(bacteria)
    counter = 1
    avg_fps = 0.0
    fps_sum = 0.0

    window = pygame.display.set_mode((Config.WIN_X, Config.WIN_Y))
    clock = pygame.time.Clock()

    while 1:
        deltat = clock.tick(Config.GAME_SPEED)
        # prepare average fps count for printing at exit
        if Config.PRINT_AVG_FPS_AT_EXIT is True:
            current_fps = clock.get_fps()
            fps_sum += current_fps
            avg_fps = fps_sum / counter
            counter += 1
        # calculate movement for each cell
        for bact in bacteria:
            if Config.CELLS_MOVING is True:
                bact.motility((Config.WIN_X, Config.WIN_Y),
                              pygame.time.get_ticks())
        # manage events
        # TODO: manage infobox and screentext as one thing (hud)
        event_control = EventControl(pygame.event.get(), bacteria,
                                     Config, pygame, infobox, screentext)
        bacteria, config, infobox, screentext = event_control.process_events()

        window.fill(Config.BACKGROUND_COLOR)
        bact_group.update(deltat)
        bact_group.draw(window)

        if infobox.shown is False:
            infobox.hide()
        else:
            infobox.show()

        if screentext.shown is True:
            screentext.show_pause_text(window)

        infobox.draw(window)

        pygame.display.flip()


if __name__ == "__main__":
    main()
