"""Prime number Game."""

import prompt
import random
import math

from brain_games.cli import welcome_user
from brain_games.check_answer import check_answer


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


def main():
    """Calculator Game function.
    Print task three times
    """
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    n_times = 0
    while n_times < 3:
        user_answer, correct_answer = print_random_number()
        counter = check_answer(user_answer, correct_answer, counter)
        n_times += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))
        if counter == -1:
            print("Let\'s try again, {}!".format(name))
            break


if __name__ == '__main__':
    main()