# Roman Numbers
# Show numbers from 1-10 in roman style
# Anatoli Penev
# 30.11.2017


# Ask the user to enter a number within the range of 1-10
def main():
    number = int(input('Enter a number within the range of 1 through 10: '))
    value(number)


def value(number):
    if number == 1:
        print('The Roman Numeral is I.')
    elif number == 2:
        print('The Roman Numeral is II.')
    elif number == 3:
        print('The Roman Numeral is III.')
    elif number == 4:
        print('The Roman Numeral is IV.')
    elif number == 5:
        print('The Roman Numeral is V.')
    elif number == 6:
        print('The Roman Numeral is VI.')
    elif number == 7:
        print('The Roman Numeral is VII.')
    elif number == 8:
        print('The Roman Numeral is VIII.')
    elif number == 9:
        print('The Roman Numeral is IX.')
    elif number == 10:
        print('The Roman Numeral is X.')
    else:
        print('This shows only numbers 1-10')


# Call the main function.
main()
