class Settings:
    """A class to store all settings for Alien invasion game"""

    def __init__(self):
        """Initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (38, 56, 66)

        # Ship settings
        self.ship_speed = 1.5
