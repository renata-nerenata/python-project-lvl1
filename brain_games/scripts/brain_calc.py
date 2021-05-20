"""Calculator Game."""
from brain_games.main_flow import flow
from brain_games.games.brain_calc_game import brain_calc_game


def main():
    """Parity Game function.
    Print task three times
    """
    open_phrase, game = brain_calc_game()
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
