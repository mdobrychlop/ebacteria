import pygame
import Config

pygame.font.init()


class InfoBox():
    """
    Simple frame that displays information on a highlighted cell.
    """
    def __init__(self):
        self.height = int(Config.WIN_Y/5)
        self.width = Config.WIN_X
        self.color = Config.HUD_COLOR
        self.position = (0, Config.WIN_Y-self.height)
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.color)
        self.surface.set_alpha(Config.HUD_TRANSPARENCY)
        self.surface.set_colorkey((0, 0, 0))
        self.shown = False
        self.text = ""
        self.curr_textpos = 0

    def draw(self, screen):
        """
        Renders the box on the screen's surface.
        """
        screen.blit(self.surface, self.position)

    def add_text(self):
        """
        Renders text on the surface of the box.
        """
        font_size = 12
        myfont = pygame.font.SysFont("monospace", font_size)
        label = myfont.render(self.text, 1, (1, 1, 1))
        self.surface.blit(label, (5, 5))

    def hide(self):
        """
        Makes the box completely transparent.
        """
        self.surface.fill((0, 0, 0))

    def show(self):
        """
        Displays the box and information.
        """
        self.surface.fill(self.color)
        self.add_text()

    def show_info(self, bact):
        info = "Specimen ID: "+str(bact.id)
        self.text = info


class PauseText():
    def show(self, screen):
        font_size = 22
        myfont = pygame.font.SysFont("monospace", font_size)
        label = myfont.render("GAME PAUSED", 1, (125, 1, 1))
        screen.blit(label, (5, 5))
