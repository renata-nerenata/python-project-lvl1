"""Calculator Game."""

import prompt
import random
import operator
from brain_games.main_flow import flow


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


def main():
    """Parity Game function.
    Print task three times
    """
    open_phrase = 'What is the result of the expression?'
    game = print_random_expression
    flow(open_phrase, game)


if __name__ == '__main__':
    main()
