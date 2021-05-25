"""Arithmetic progression Game."""

from brain_games.main_flow import flow
from brain_games.games import brain_progression


def main():
    """Progression Game function.
    Print task three times
    """
    game = brain_progression
    flow(game)


if __name__ == '__main__':
    main()
