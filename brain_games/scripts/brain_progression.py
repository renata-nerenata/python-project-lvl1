"""Arithmetic progression Game."""

from brain_games.main_flow import flow
from brain_games.games.brain_progression import brain_progression_game


def main():
    """Progression Game function.
    Print task three times
    """
    open_phrase, game = brain_progression_game()
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
