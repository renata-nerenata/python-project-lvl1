"""Greatest common divisor Game."""

import prompt
import random
import math

from brain_games.cli import welcome_user
from brain_games.check_answer import check_answer


def print_random_gcd():
    """Engine of the Game."""
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    print('Question: {} {}'.format(number_a, number_b))
    user_answer = prompt.string('Your answer: ')
    correct_answer = str(math.gcd(number_a, number_b))
    return user_answer, correct_answer


def main():
    """Calculator Game function.
    Print task three times
    """
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    n_times = 0
    while n_times < 3:
        user_answer, correct_answer = print_random_gcd()
        counter = check_answer(user_answer, correct_answer, name, counter)
        n_times += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()