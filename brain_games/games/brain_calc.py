"""Calculator Game."""

import random
import operator


PHRASE_RULE = 'What is the result of the expression?'


def get_question_and_answer():
    """
    Generate random expression and correct answer for calculator game
    Returns:
        question: a generated expression
        correct_answer: correct answer for the expression
    """
    number_a = random.randint(1, 10)
    number_b = random.randint(1, 10)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    random_operator = random.choice(list(operators.keys()))
    question_expression = '{} {} {}'.format(number_a, random_operator, number_b)
    correct_answer = str(operators.get(random_operator)(number_a, number_b))
    return question_expression, correct_answer
