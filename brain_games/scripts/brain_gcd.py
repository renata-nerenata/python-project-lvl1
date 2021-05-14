"""Greatest common divisor Game."""

import prompt
import random
import math
from brain_games.main_flow import flow


def print_random_gcd():
    """Engine of the Game."""
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    print('Question: {} {}'.format(number_a, number_b))
    user_answer = prompt.string('Your answer: ')
    correct_answer = str(math.gcd(number_a, number_b))
    return user_answer, correct_answer


def main():
    """Greatest common divisor Game function.
    Print task three times
    """
    open_phrase = 'Find the greatest common divisor of given numbers.'
    game = print_random_gcd
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
