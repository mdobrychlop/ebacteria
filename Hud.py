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
        # text is a list of lines to display
        self.text = []
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
        vertical_position = 5
        font_size = 12
        spacing = int(font_size / 4)

        for line in self.text:
            myfont = pygame.font.SysFont("monospace", font_size)
            label = myfont.render(line, 1, (1, 1, 1))
            self.surface.blit(label, (5, vertical_position))
            vertical_position += font_size + spacing

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
        id_info = "Specimen ID: "+str(bact.id)
        speed_info = "speed: "+str(bact.original_speed)
        self.text = [id_info, speed_info]


class ScreenText():
    """
    Controls text that is displayed directly on the screen surface.
    """
    def __init__(self):
        self.shown = False

    def show_pause_text(self, screen):
        font_size = 22
        myfont = pygame.font.SysFont("monospace", font_size)
        label = myfont.render("GAME PAUSED", 1, (125, 1, 1))
        screen.blit(label, (10, 10))

    def hide_pause_text(self, screen):
        pass
