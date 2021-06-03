"""Parity Game."""


from brain_games.main import flow
from brain_games.games import brain_even


def main():
    """Parity Game function.
    Print task three times
    """
    flow(brain_even)


if __name__ == '__main__':
    main()
