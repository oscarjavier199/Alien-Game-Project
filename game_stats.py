

class GameStats:
    """Track statistics for alien invasion"""
    def __init__(self, ai_game):
        """Initialize statistics"""

        self.level = 1
        self.score = 0
        self.ships_left = None
        self.settings = ai_game.settings
        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that cam change during the game."""
        self.ships_left = self.settings.ship_limit
