from game import Game
from player import ComputerPlayer


def main():
    print('Running game')
    jason = ComputerPlayer(name='Jason')
    zack = ComputerPlayer(name='Zack')
    game = Game(players=[jason, zack])
    game.run()


if __name__ == '__main__':
    main()
