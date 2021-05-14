"""Main flow."""

from brain_games.cli import welcome_user
from brain_games.check_answer import check_answer
from brain_games.congrats import congrats_or_fail


def flow(open_phrase, game):
    """Main flow of each game
    """
    name = welcome_user()
    print(open_phrase)
    counter = 0
    while counter < 3:
        user_answer, correct_answer = game()
        counter = check_answer(user_answer, correct_answer, counter)
        congrats_or_fail(counter, name)
        if counter == -1:
            break
