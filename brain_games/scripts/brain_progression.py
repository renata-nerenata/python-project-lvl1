"""Arithmetic progression Game."""

import prompt
import random
from brain_games.main_flow import flow


def print_random_progression():
    """Engine of the Game."""
    number_start = random.randint(1, 100)
    number_dif = random.randint(1, 20)
    number_elements = random.randint(5, 10)
    progression_list = []
    for i in range(1, number_elements + 1):
        progression_list.append(number_start)
        number_start = number_start + number_dif
    lost_item = random.randint(0, number_elements - 1)
    correct_answer = str(progression_list[lost_item])
    progression_list[lost_item] = '..'
    progression_list_str = ' '.join(str(x) for x in progression_list)
    print('Question: {}'.format(progression_list_str))
    user_answer = prompt.string('Your answer: ')
    return user_answer, correct_answer


def main():
    """Progression Game function.
    Print task three times
    """
    open_phrase = 'What number is missing in the progression?'
    game = print_random_progression
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
