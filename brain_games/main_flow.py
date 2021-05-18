"""Main flow."""

from brain_games.congrats import congrats_or_fail
from brain_games.first_question import open_game


def check_answer(user_answer, correct_answer, counter):

    """Check right answer function.
        Args:
            user_answer: input user answer
            correct_answer: right answer
            name: user name
            counter: counter of right answers
        Returns:
            str answer
    """
    if user_answer == correct_answer:
        counter += 1
        print("Correct!")
        return counter
    else:
        print("'{}' is wrong answer ;(.".format(user_answer))
        print("Correct answer was '{}'".format(correct_answer))
        return -1


def flow(open_phrase, game):
    name = open_game(open_phrase)
    counter = 0
    while counter < 3:
        user_answer, correct_answer = game()
        counter = check_answer(user_answer, correct_answer, counter)
        congrats_or_fail(counter, name)
        if counter == -1:
            break
