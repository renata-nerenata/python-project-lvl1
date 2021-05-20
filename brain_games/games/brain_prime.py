import prompt
import random
import math


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


def print_random_number():
    """Engine of the Game."""
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    user_answer = prompt.string('Your answer: ')
    correct_answer = str(is_prime(number))
    return user_answer, correct_answer


def brain_prime_game():
    """Prime Game function.
    Print task three times
    """
    open_phrase = 'Answer "yes" if given number is prime. Otherwise answer "no"'
    game = print_random_number
    return open_phrase, game
