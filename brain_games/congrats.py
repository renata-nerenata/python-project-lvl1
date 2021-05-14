"Print congrats"


def congrats_or_fail(counter, name):
    if counter == 3:
        print('Congratulations, {}!'.format(name))
    if counter == -1:
        print("Let\'s try again, {}!".format(name))