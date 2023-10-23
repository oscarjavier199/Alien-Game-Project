class Settings:
    """A class to store all settings for Alien invasion game"""

    def __init__(self):
        """Initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (38, 56, 66)

        # Ship settings
        self.ship_speed = 4.1
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (240, 0, 1)
        self.bullets_allowed = 3

        # Aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1