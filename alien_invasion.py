import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        # pygame.display.set_mode() creates a display window, which will be 1,200 pixels wide by 800 pixels high\
        self.clock = pygame.time.Clock()
        # Instance of settings file
        self.settings = Settings()
        # Screen width and height (from settings file)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Title of the window
        pygame.display.set_caption("Alien Invasion")
        # instance of ship file
        self.ship = Ship(self)

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # Call to helper method _check_events:
            self._check_events()
            # Call to helper method _update_screen:
            self._update_screen()
            # Run the game at 60 fps
            self.clock.tick(60)

    # helper method to refactor the code
    def _check_events(self):
        """Responds to key presses and mouse events"""
        for event in pygame.event.get():
            # if player clicks the windows close button sys.exit() will exit the game
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        # Fills the color of the pygame window
        self.screen.fill(self.settings.bg_color)
        # Draw the ship to the screen
        self.ship.blitme()
        # make the most recently drawn screen visible, (updates the display)
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
