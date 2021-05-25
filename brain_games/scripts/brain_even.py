"""Parity Game."""


from brain_games.main_flow import flow
from brain_games.games import brain_even


def main():
    """Parity Game function.
    Print task three times
    """
    game = brain_even
    flow(game)


if __name__ == '__main__':
    main()
