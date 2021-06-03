"""Prime number Game."""

from brain_games.main import flow
from brain_games.games import brain_prime


def main():
    """Prime Game function.
    Print task three times
    """
    flow(brain_prime)


if __name__ == '__main__':
    main()
