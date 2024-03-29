"""Arithmetic progression Game."""

import random


PHRASE_RULE = 'What number is missing in the progression?'


def get_question_and_answer():
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
    question_expression = '{}'.format(progression_list_str)
    return question_expression, correct_answer
