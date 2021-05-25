"""Greatest common divisor Game."""

from brain_games.main_flow import flow
from brain_games.games import brain_gcd


def main():
    """Greatest common divisor Game function.
    Print task three times
    """
    game = brain_gcd
    flow(game)


if __name__ == '__main__':
    main()
