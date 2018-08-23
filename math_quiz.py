# Math quiz
# Random math questions
# Anatoli Penev
# 15.12.1017


def main():
    from random import randint
    number1 = randint(1, 1000)
    number2 = randint(1, 1000)
    print("What is " + str(number1) + " + " + str(number2) + " ?: ")
    total = number1 + number2
    answer = int(input('Enter the answer: '))
    check(answer, total)


def check(answer, total):
        if answer == total:
            print('Congratulation!')
        else:
            print('The answer is', total)


main()

