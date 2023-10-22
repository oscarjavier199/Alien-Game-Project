import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


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

        # instance of bullets file
        self.bullets = pygame.sprite.Group()

    # Method to run the game
    def run_game(self):
        """start the main loop for the game."""
        while True:
            # Call to helper method _check_events:
            self._check_events()
            # Checks if user is pressing right arrow key (from ship.py)
            self.ship.update()
            self._update_bullets()
            # Call to helper method _update_screen:
            self._update_screen()
            # Run the game at 60 fps
            self.clock.tick(60)

    # helper method to refactor the code
    def _check_events(self):
        """Responds to key presses and mouse events"""
        for event in pygame.event.get():
            print(event)
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    # Helper method to check when keys are released
    def _check_keyup_events(self, event):
        """ Responds with key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # Helper method to create bullets
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # Helper method to update bullets position
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet position
        self.bullets.update()

        # Get rid of bullets that have disappeared to save memory
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    # Helper method to update the images on the screen
    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        # Fills the color of the pygame window
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the ship to the screen
        self.ship.blitme()
        # make the most recently drawn screen visible, (updates the display)
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
