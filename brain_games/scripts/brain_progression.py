"""Arithmetic progression Game."""

import prompt
import random

from brain_games.cli import welcome_user
from brain_games.check_answer import check_answer


def print_random_progression():
    """Engine of the Game."""
    number_start = random.randint(1, 100)
    number_dif = random.randint(1, 20)
    number_elements = random.randint(5, 10)
    progression_list = []
    for i in range(1, number_elements + 1):
        progression_list.append(number_start)
        number_start = number_start+number_dif
    lost_item = random.randint(0, number_elements-1)
    correct_answer = str(progression_list[lost_item])
    progression_list[lost_item] = '..'
    print('Question: {}'.format(progression_list))
    user_answer = prompt.string('Your answer: ')
    return user_answer, correct_answer


def main():
    """Calculator Game function.
    Print task three times
    """
    name = welcome_user()
    print('What number is missing in the progression?')
    counter = 0
    n_times = 0
    while n_times < 3:
        user_answer, correct_answer = print_random_progression()
        counter = check_answer(user_answer, correct_answer, name, counter)
        n_times += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()