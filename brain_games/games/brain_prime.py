"""Prime number Game."""

import random
import math


open_phrase = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(number):
    """Check prime number
    Args:
        number: the random number
    Returns:
        str answer
    """
    if number == 2:
        return 'yes'
    if number % 2 == 0 or number <= 1:
        return 'no'
    sqr = int(math.sqrt(number)) + 1
    for divisor in range(3, sqr, 2):
        if number % divisor == 0:
            return 'no'
    return 'yes'


def get_question_and_answer():
    """Engine of the Game."""
    number = random.randint(1, 100)
    question = 'Question: {}'.format(number)
    correct_answer = str(is_prime(number))
    return question, correct_answer


def brain_prime_game():
    """Prime Game function.
    Print task three times
    """
    return get_question_and_answer
