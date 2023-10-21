import pygame
import sys

from settings_2 import Settings_2
from mario import Character

class Image:

    """ A class to draw a character to the screen"""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("It's-a-me Mario!")
        self.settings = Settings_2()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.mario = Character(self)

    def run_game(self):
        """Starts the main loop to run the game"""
        self._update_screen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

# Helper method  to update the screen
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.mario.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    TY = Image()
    TY.run_game()
