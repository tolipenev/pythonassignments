# Rock paper scissors
# Python program for the popular game rock, paper, scissors
# Anatoli Penev
# 15.12.1017


def main():
    com, choice = set_up()
    rule(com, choice)


def set_up():
    import random
    n = random.randrange(1, 4)
    com = ''
    if n == 1:
        com = 'rock'
    elif n == 2:
        com = 'scissors'
    else:
        com = 'paper'
    choice = input('Choose and enter one among \'rock\', \'scissors\' or' '\'paper\': ')
    print(com)
    return com, choice


def rule(com, choice):
    while com == choice:
        com, choice = set_up()
    else:
        if com == 'rock' and choice == 'scissors':
            print('Computer wins!')
        elif com == 'scissors' and choice == 'rock':
            print('You win!')
        elif com == 'paper' and choice == 'scissors':
            print('You wins!')
        elif com == 'scissors' and choice == 'paper':
            print('Computer wins!')
        elif com == 'rock' and choice == 'paper':
            print('You win!')
        elif com == 'paper' and choice == 'rock':
            print('Computer wins!')


main()
