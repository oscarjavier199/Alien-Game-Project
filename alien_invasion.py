import sys
import pygame

from settings import Settings


class AlienInvasion:
    '''class to manage game assets and behavior'''

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        # pygame.display.set_mode() creates a display window, which will be 1,200 pixels wide by 800 pixels high\
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #change background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # keyboard and mouse events
            for event in pygame.event.get():
                #if player clicks the windows's close button sys.exit() will exit the game
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            # make the most recently drawn screen visible, (updates the display)
            pygame.display.flip()
            # Run the game at 60 fps
            self.clock.tick(60)


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
