# Sum of Digits in a String
# Final sum of digits entered in a string
# Anatoli Penev
# 11.01.2018


def main():
    numbers = input('Please enter singe digits: ')
    if numbers.isdigit():
        print('The string contains only digits.')
    if numbers.isalpha():
        print('The string contains only alphabetic characters.')
    if numbers.isspace():
        print('The string contains only whitespace characters.')
    if numbers.islower():
        print('The letters in the string are all lowercase.')
    if numbers.isupper():
        print('The letters in the string are all uppercase.')
    digit_sum(numbers)


def digit_sum(numbers):
    total = 0

    try:
        for i in numbers:
            total += int(i)
        print("The total sum of the numbers entered is :", total)
    except ValueError as error:
        print("Only digits are allowed!", error)
        main()


main()
