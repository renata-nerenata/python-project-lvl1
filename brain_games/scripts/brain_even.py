"""Parity Game."""

import prompt
import random
from brain_games.cli import welcome_user
from brain_games.check_answer import check_answer


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


def print_random_number():
    """Engine of the Game."""
    number = random.randint(1, 99)
    print('Question:', number)
    user_answer = str(prompt.string('Your answer: '))
    correct_answer = str(even_number(number))
    return user_answer, correct_answer


def main():
    """Parity Game function.
    Print task three times
    """
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
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