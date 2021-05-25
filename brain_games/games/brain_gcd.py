"""Greatest common divisor Game."""

import prompt
import random
import math


open_phrase = 'Find the greatest common divisor of given numbers.'


def print_random_expression():
    """Engine of the Game."""
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    print('Question: {} {}'.format(number_a, number_b))
    user_answer = prompt.string('Your answer: ')
    correct_answer = str(math.gcd(number_a, number_b))
    return user_answer, correct_answer


def brain_gcd_game():
    """Greatest common divisor Game function.
    Print task three times
    """
    game = print_random_expression
    return game
