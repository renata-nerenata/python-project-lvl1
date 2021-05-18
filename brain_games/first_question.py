"Print greetings"

from brain_games.cli import welcome_user


def open_game(open_phrase):
    """Main flow of each game
    """
    name = welcome_user()
    print(open_phrase)
    return name
