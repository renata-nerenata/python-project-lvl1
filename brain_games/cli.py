"""This is the welcome script."""

import prompt


def welcome_user():
    """Return a welcome line.

    Returns:
        name of user
    """
    name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!\nHello, {}'.format(name))
    return name
