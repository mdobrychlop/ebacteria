from pygame.locals import *
import sys
import random


class EventControl():
    """
    Controls the game's events, e.g. what happens when
    a mouse button is pressed, or when a keyboard key
    is pressed (well, for now it's only that).
    Later, if more events are used, it'd be a good idea
    to separate "user input events" from other events.
    """
    def __init__(self, events, bacteria, config, pygame, hud):
        self.events = events
        self.hud = hud
        self.bacteria = bacteria
        self.config = config
        self.pygame_state = pygame
        self.isPaused = False

    def process_events(self):
        """
        Gathers and processes all events and returns
        changed lists of bacteria and game parameters.
        """
        for self.event in self.events:
            self.manage_mouse()
            if not hasattr(self.event, 'key'):
                continue
            self.manage_keyboard()
        return self.bacteria, self.config, self.hud

    def manage_mouse(self):
        """
        Gathers all methods devoted to proess mouse input.
        """
        self.mouse_bacteria()

    def manage_keyboard(self):
        """
        Gathers all methods devoted to proess keyboard input.
        """
        self.key_pause()
        self.key_quit()

    def mouse_bacteria(self):
        """
        Decides what happens after clicking on a bacterium cell.
        Temporarily, for testing purposes, it randomly colors
        a clicked cell.
        """
        if (self.event.type == self.pygame_state.MOUSEBUTTONDOWN and
                self.event.button == 1):

            pos = self.pygame_state.mouse.get_pos()

            clicked_on_bacterium = False
            # prev_clicked_bact = None

            for bact in self.bacteria:
                bact.highlighted = False
                if bact.rect.collidepoint(pos):
                    clicked_on_bacterium = True
                    self.mouse_hud_show()
                    self.hud.show_info(bact)
                    bact.highlighted = True
                    prev_clicked_bact = self.bacteria.index(bact)
                bact.draw_from_shapes()

            if clicked_on_bacterium is False:
                self.mouse_hud_hide()

    def mouse_hud_show(self):
        self.hud.shown = True

    def mouse_hud_hide(self):
        self.hud.shown = False

    def key_pause(self):
        """
        Controls game pausing and unpausing using keyboard.
        """
        if (self.event.type == self.pygame_state.KEYDOWN and
                self.event.key == K_p):

            if self.config.CELLS_MOVING is True:
                    self.config.CELLS_MOVING = False
                    for bact in self.bacteria:
                        bact.speed = 0
            else:
                self.config.CELLS_MOVING = True

    def key_quit(self):
        """
        Controls exiting the game using keyboard.
        """
        if (self.event.type == self.pygame_state.QUIT or
                self.event.key == K_ESCAPE):

            self.pygame_state.quit()
            sys.exit()
