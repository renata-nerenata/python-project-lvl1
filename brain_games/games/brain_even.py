"""Parity Game."""

import prompt
import random


open_phrase = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_number(number):
    """Parity function.

    Args:
        number: the random number
    Returns:
        str answer
    """
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def print_random_expression():
    """Engine of the Game."""
    number = random.randint(1, 99)
    print('Question:', number)
    user_answer = str(prompt.string('Your answer: '))
    correct_answer = str(even_number(number))
    return user_answer, correct_answer


def brain_even_game():
    """Parity Game function.
    Print task three times
    """

    game = print_random_expression
    return game
