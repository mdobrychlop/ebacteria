from pygame.locals import *
from pygame import gfxdraw
from Bacterium import Bacterium
import math
import pygame
import random
import sys

# --- MAIN PARAMETERS ---
# game window
WIN_X = 800
WIN_Y = 600
BACKGROUND_COLOR = (150, 150, 150)
PRINT_AVG_FPS_AT_EXIT = True

# number of iterations of the main loop per second
# this also limits the number of frames per second
GAME_SPEED = 60

# bacteria's appearance and behavior
NUMBER_OF_CELLS = 10
CELL_SIZE = 8  # tip: cells look better when even number
CELLS_MOVING = True  # False freezes all movement
CELLS_NON_ROTATED = False  # True makes cells start from non-rotated positions
PNG_IMAGE = ''  # 'black_test3.png'  # empty string if drawing using shapes
MORPHOLOGY = 'bacillus'  # in case drawing using pygame's shapes
CELL_COLOR = (50, 50, 50)  # in case drawing using pygame's shapes
# --- --------------- ---

# generate all bacteria objects
bacteria = []
for i in range(NUMBER_OF_CELLS):
    draw_coord = (random.randrange(50, WIN_X-50),
                  random.randrange(50, WIN_Y-50))

    if CELLS_NON_ROTATED is False:
        draw_direction = random.randrange(-180, 180)
    else:
        draw_direction = 0

    # multiplier is a float that has to be truncated to 1 digit after the dot
    # otherwise the game freezes right after generating initial positions
    multipl = random.uniform(0.1, 1.5)
    multipl = float(str(multipl)[:3])

    bact = Bacterium(draw_coord, draw_direction, PNG_IMAGE,
                     multipl, MORPHOLOGY, CELL_SIZE, CELL_COLOR)
    bacteria.append(bact)

bact_group = pygame.sprite.RenderPlain(bacteria)

counter = 1
avg_fps = 0.0
fps_sum = 0.0

window = pygame.display.set_mode((WIN_X, WIN_Y))
clock = pygame.time.Clock()

while 1:
    deltat = clock.tick(GAME_SPEED)

    # prepare average fps count for printing at exit
    if PRINT_AVG_FPS_AT_EXIT is True:
        current_fps = clock.get_fps()
        fps_sum += current_fps
        avg_fps = fps_sum / counter
        counter += 1

    for bact in bacteria:
        if CELLS_MOVING is True:
            bact.motility((WIN_X, WIN_Y), pygame.time.get_ticks())

    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            continue
        if event.type == pygame.QUIT or event.key == K_ESCAPE:
            if PRINT_AVG_FPS_AT_EXIT is True:
                print("AVERAGE FPS AFTER", counter, "ITERATIONS:", avg_fps)
            pygame.quit()
            sys.exit()

    window.fill(BACKGROUND_COLOR)
    bact_group.update(deltat)
    bact_group.draw(window)
    pygame.display.flip()
