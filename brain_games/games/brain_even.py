"""Parity Game."""

import random


PHRASE_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Parity function.

    Args:
        number: the random number
    Returns:
        str answer
    """
    if number % 2 == 0:
        return True
    else:
        return False


def answer_reshape(number):
    """Transform Bool value to string answer"""
    if is_even(number):
        return 'yes'
    return 'no'


def get_question_and_answer():
    """Engine of the Game."""
    number = random.randint(1, 99)
    question_expression = '{}'.format(number)
    correct_answer = str(answer_reshape(number))
    return question_expression, correct_answer


def brain_even_game():
    """Parity Game function.
    Print task three times
    """

    return get_question_and_answer
