"""Prime number Game."""

from brain_games.main_flow import flow
from brain_games.games.brain_prime import brain_prime_game


def main():
    """Prime Game function.
    Print task three times
    """
    open_phrase, game = brain_prime_game()
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
