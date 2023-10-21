import pygame

class Character:

    def __init__(self, TY_game):
        """Initialize the image and starting position"""
        self.screen = TY_game.screen
        # Access screen's rect attribute using get_rect()
        self.screen_rect = TY_game.screen.get_rect()

        # Load the image and its rectangle
        self.image = pygame.image.load('../images/mario_wonder_artwork.jpg')
        default_image_size = (200, 200)
        self.image = pygame.transform.scale(self.image, default_image_size)
        self.rect = self.image.get_rect()

        # Image position
        self.rect.center = self.screen_rect.center


    def blitme(self):
        """Draws image to current location"""
        self.screen.blit(self.image, self.rect)
