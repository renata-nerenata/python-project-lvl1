"""Greatest common divisor Game."""

import random
import math


open_phrase = 'Find the greatest common divisor of given numbers.'


def print_random_expression():
    """Engine of the Game."""
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    question = 'Question: {} {}'.format(number_a, number_b)
    correct_answer = str(math.gcd(number_a, number_b))
    return question, correct_answer


def brain_gcd_game():
    """Greatest common divisor Game function.
    Print task three times
    """
    game = print_random_expression
    return game
