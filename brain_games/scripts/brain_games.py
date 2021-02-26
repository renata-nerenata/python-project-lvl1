#!/usr/bin/env python
import prompt


def main():
    """Return a welcome line.

    Returns:
        name of user
    """
    name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!\nHello, {}'.format(name))
    return name


if __name__ == '__main__':
    main()
