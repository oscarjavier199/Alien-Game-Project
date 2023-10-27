class Settings:
    """A class to store all settings for Alien invasion game"""

    def __init__(self):
        """Initialize the game's static settings"""

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

        # How quicly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 6.0
        self.bullet_speed = 7.0
        self.alien_speed = 3.0

        # Fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

