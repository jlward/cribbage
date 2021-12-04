class PlayerWon(Exception):
    def __init__(self, player):
        self.player = player
