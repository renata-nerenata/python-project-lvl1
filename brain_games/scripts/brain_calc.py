"""Calculator Game."""
from brain_games.games import brain_calc
from brain_games.main import flow


def main():
    """Parity Game function.
    Print task three times
    """
    flow(brain_calc)


if __name__ == '__main__':
    main()
