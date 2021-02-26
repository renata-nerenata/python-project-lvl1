"""Calculator Game."""

import prompt
import random
import operator

from brain_games.cli import welcome_user
from brain_games.check_answer import check_answer


def print_random_expression():
    """Engine of the Game."""
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    oper = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul}
    expression = random.choice(list(oper.keys()))
    print('Question: {}{}{}'.format(number_a, expression, number_b))
    user_answer = prompt.string('Your answer: ')
    correct_answer = str(oper.get(expression)(number_a, number_b))
    return user_answer, correct_answer


def main():
    """Calculator Game function.
    Print task three times
    """
    name = welcome_user()
    print('What is the result of the expression?')
    counter = 0
    n_times = 0
    while n_times < 3:
        user_answer, correct_answer = print_random_expression()
        counter = check_answer(user_answer, correct_answer, name, counter)
        n_times += 1
        if counter == 3:
            print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()