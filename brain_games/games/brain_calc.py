"""Calculator Game."""

import random
import operator


open_phrase = 'What is the result of the expression?'


def get_question_and_answer():
    """Engine of the Game."""
    number_a = random.randint(1, 10)
    number_b = random.randint(1, 10)
    oper = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul}
    expression = random.choice(list(oper.keys()))
    question = 'Question: {} {} {}'.format(number_a, expression, number_b)
    correct_answer = str(oper.get(expression)(number_a, number_b))
    return question, correct_answer


def brain_calc_game():
    """Parity Game function.
    Print task three times
    """
    return get_question_and_answer
