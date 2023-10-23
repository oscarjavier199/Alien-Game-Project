import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


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

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        # instance of ship file
        self.ship = Ship(self)

        # instance of bullets file
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # start alien invasion in active state
        self.game_active = False

        # Make the Play button
        self.play_button = Button(self, "Play")

    # Method to run the game
    def run_game(self):
        """start the main loop for the game."""
        while True:
            # Call to helper method _check_events:
            self._check_events()
            if self.game_active:
                # Checks if user is pressing right arrow key (from ship.py)
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    # helper method to start the game when the player clicks on play
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

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
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions"""
        self._check_fleet_edges()
        """Update the positions of all aliens in the fleet."""
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    # Helper method to update the images on the screen
    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        # Fills the color of the pygame window
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw the ship to the screen
        self.ship.blitme()
        # Draw an alien to the screen
        self.aliens.draw(self.screen)
        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        # make the most recently drawn screen visible, (updates the display)
        pygame.display.flip()

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Create an alien and keep adding aliens until there's no more space
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row, reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Responds to the ship being hit by an alien"""
        if self.stats.ship_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
