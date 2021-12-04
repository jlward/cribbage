from exceptions import PlayerWon
from round import Round


class Game:
    def __init__(self, players):
        self.rounds = []
        self.players = players

    def start_round(self):
        for player in self.players:
            player.reset_hand()
        _round = Round(
            players=self.players,
        )
        _round.start()
        self.rounds.append(_round)

    def run(self):
        try:
            while True:
                self.start_round()
        except PlayerWon:
            pass
        for player in self.players:
            print(player)
