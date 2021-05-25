"""Calculator Game."""
from brain_games.games import brain_calc
from brain_games.main_flow import flow


def main():
    """Parity Game function.
    Print task three times
    """
    game = brain_calc
    flow(game)


if __name__ == '__main__':
    main()
