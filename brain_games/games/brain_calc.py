"""Calculator Game."""

import prompt
import random
import operator


open_phrase = 'What is the result of the expression?'


def print_random_expression():
    """Engine of the Game."""
    number_a = random.randint(1, 10)
    number_b = random.randint(1, 10)
    oper = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul}
    expression = random.choice(list(oper.keys()))
    print('Question: {} {} {}'.format(number_a, expression, number_b))
    user_answer = prompt.string('Your answer: ')
    correct_answer = str(oper.get(expression)(number_a, number_b))
    return user_answer, correct_answer


def brain_calc_game():
    """Parity Game function.
    Print task three times
    """
    game = print_random_expression
    return game
