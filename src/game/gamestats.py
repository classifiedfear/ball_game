class GameStats():
    def __init__(self, game):
        self.settings = game.settings
        self.game_active = False
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        self.circle_left = self.settings.circle_limit
        self.score = 0
        self.lvl = 1