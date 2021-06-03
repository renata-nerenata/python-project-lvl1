"""Main flow."""

from brain_games.cli import welcome_user
import prompt


def flow(game):
    name = welcome_user()
    print(game.PHRASE_RULE)
    game_counter = 0
    game_limit = 3
    while game_counter < game_limit:
        question_expression, correct_answer = game.get_question_and_answer()
        print('Question: {}'.format(question_expression))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            game_counter += 1
            print("Correct!")
        else:
            print("'{}' is wrong answer ;(.".format(user_answer))
            print("Correct answer was '{}'".format(correct_answer))
            print("Let\'s try again, {}!".format(name))
            break
    if game_counter == 3:
        print('Congratulations, {}!'.format(name))
