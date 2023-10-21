import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        # We access screen's rect attribute using get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and its rectangle (rect)
        self.image = pygame.image.load('images/spaceship.pod_.1.green_.png')
        DEFAULT_IMAGE_SIZE = (100, 100)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
