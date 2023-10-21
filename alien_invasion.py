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

        # Run game in full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

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
            # Checks if user is pressing right arrow key (from ship.py)
            self.ship.update()
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
            # Check if user clicks the right arrow key (KEYDOWN events)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # if user stops pressing right-left key ship will stop moving (KEYUP events)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # Helper method to check when keys are being pressed
    def _check_keydown_events(self, event):
        """ Responds to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # If player presses q, game quits
        elif event.key == pygame.K_q:
            sys.exit()

    # Helper method to check when keys are released
    def _check_keyup_events(self, event):
        """ Responds with key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


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
