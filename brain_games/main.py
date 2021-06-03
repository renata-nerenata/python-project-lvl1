"""Main flow."""

from brain_games.cli import welcome_user
import prompt


def check_answer(user_answer, correct_answer):
    """Check right answer function.
        Args:
            user_answer: input user answer
            correct_answer: right answer
            counter: counter of right answers
        Returns:
            bool answer
    """
    if user_answer == correct_answer:
        return True
    return False


def comment_answer(user_answer, correct_answer, game_counter):
    """
    Comment answer function.
        Args:
            user_answer: input user answer
            correct_answer: right answer
            game_counter: counter of right answers
        Returns:
            int game_counter
        """
    if check_answer(user_answer, correct_answer):
        game_counter += 1
        print("Correct!")
        return game_counter
    print("'{}' is wrong answer ;(.".format(user_answer))
    print("Correct answer was '{}'".format(correct_answer))
    return -1


def congrats_or_fail(counter, name, game_limit, game_fail_marker):
    """
    Print congratulation or fail phrase
    """
    if counter == game_limit:
        print('Congratulations, {}!'.format(name))
    if counter == game_fail_marker:
        print("Let\'s try again, {}!".format(name))


def flow(game):
    name = welcome_user()
    print(game.PHRASE_RULE)
    game_counter = 0
    game_limit = 3
    game_fail_marker = -1
    while game_counter < game_limit:
        question_expression, correct_answer = game.get_question_and_answer()
        print('Question: {}'.format(question_expression))
        user_answer = prompt.string('Your answer: ')
        game_counter = comment_answer(user_answer, correct_answer, game_counter)
        congrats_or_fail(game_counter, name, game_limit, game_fail_marker)
        if game_counter == game_fail_marker:
            break
