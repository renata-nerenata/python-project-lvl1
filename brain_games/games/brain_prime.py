"""Prime number Game."""

import random
import math


PHRASE_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(number):
    """Check prime number
    Args:
        number: the random number
    Returns:
        str answer
    """
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False
    sqr = int(math.sqrt(number)) + 1
    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return False
    return True


def answer_reshape(number):
    """Transform Bool value to string answer"""
    if is_prime(number):
        return 'yes'
    return 'no'


def get_question_and_answer():
    """Engine of the Game."""
    number = random.randint(1, 100)
    question_expression = '{}'.format(number)
    correct_answer = answer_reshape(number)
    return question_expression, correct_answer
