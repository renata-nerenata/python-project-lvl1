"""Parity Game."""


from brain_games.main_flow import flow
from brain_games.games.brain_even import brain_even_game


def main():
    """Parity Game function.
    Print task three times
    """
    open_phrase, game = brain_even_game()
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
