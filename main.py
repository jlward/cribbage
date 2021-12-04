import argparse
from collections import defaultdict

from game import Game
from player import ComputerPlayer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--num-games',
        default=1,
        type=int,
    )
    args = parser.parse_args()

    print('Running game')
    winners = defaultdict(int)
    for _ in range(args.num_games):
        jason = ComputerPlayer(name='Jason')
        zack = ComputerPlayer(name='Zack')
        game = Game(players=[jason, zack])
        player = game.run()
        winners[player.name] += 1
    print(winners)


if __name__ == '__main__':
    main()
