"""Prime number Game."""

from brain_games.main_flow import flow
from brain_games.games import brain_prime


def main():
    """Prime Game function.
    Print task three times
    """
    game = brain_prime
    flow(game)


if __name__ == '__main__':
    main()
