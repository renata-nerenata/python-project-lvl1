"""Greatest common divisor Game."""

import random
import math


PHRASE_RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    """Engine of the Game."""
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    question_expression = '{} {}'.format(number_a, number_b)
    correct_answer = str(math.gcd(number_a, number_b))
    return question_expression, correct_answer


def brain_gcd_game():
    """Greatest common divisor Game function.
    Print task three times
    """
    return get_question_and_answer
