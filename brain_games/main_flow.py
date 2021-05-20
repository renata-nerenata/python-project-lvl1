"""Main flow."""

from brain_games.cli import welcome_user


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


def congrats_or_fail(counter, name):
    """
    Print congratulation or fail phrase
    """
    if counter == 3:
        print('Congratulations, {}!'.format(name))
    if counter == -1:
        print("Let\'s try again, {}!".format(name))


def flow(open_phrase, game):
    name = welcome_user()
    print(open_phrase)
    counter = 0
    while counter < 3:
        user_answer, correct_answer = game()
        counter = check_answer(user_answer, correct_answer, counter)
        congrats_or_fail(counter, name)
        if counter == -1:
            break
