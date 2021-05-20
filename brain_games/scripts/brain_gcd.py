"""Greatest common divisor Game."""

from brain_games.main_flow import flow
from brain_games.games.brain_gcd_game import brain_gcd_game


def main():
    """Greatest common divisor Game function.
    Print task three times
    """
    open_phrase, game = brain_gcd_game()
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
