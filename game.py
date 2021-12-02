from player import ComputerPlayer
from round import Round


class Game:
    def __init__(self):
        self.rounds = []
        self.players = []

    def create_players(self):
        self.players.append(ComputerPlayer(name='Jason'))
        self.players.append(ComputerPlayer(name='Zack'))

    def start_round(self):
        _round = Round(
            players=self.players,
        )
        _round.start()
        self.rounds.append(_round)

    def run(self):
        self.create_players()
        self.start_round()
