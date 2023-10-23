class GameStats:
    """Track statistics for alien invasion"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings

    def reset_stats(self):
        """Initialize statistics that cam change during the game."""
        self.ships_left = self.settings.ship_limit
