"""This is script helps check up user answer."""


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
        print("'{}' is wrong answer ;(. Correct answer was '{}'".format(user_answer, correct_answer))
        return -1

if __name__ == '__main__':
    check_answer(user_answer, correct_answer, name)