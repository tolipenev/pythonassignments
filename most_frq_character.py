# Most frequent character
# Display a character that appears the most in a string
# Anatoli Penev
# 11.01.2018


def main():
    while 1:
        user_entry = input('Please enter a phrase or sentence: ')
        if check(user_entry):
            break
    if user_entry.isalnum():
        print('The string is alphanumeric.')
    if user_entry.isdigit():
        print('The string contains only digits.')
    if user_entry.isalpha():
        print('The string contains only alphabetic characters.')
    if user_entry.isspace():
        print('The string contains only whitespace characters.')
    if user_entry.islower():
        print('The letters in the string are all lowercase.')
    if user_entry.isupper():
        print('The letters in the string are all uppercase.')
    most_common(user_entry)


def check(s):
    import re
    try:
        if not re.match("^[A-Za-z0-9_-]*$", s):
            raise TypeError
        return True
    except TypeError:
        print("Only digits and letters are accepted!")
        return False


def most_common(user_entry):
    count = 0
    top = ""
    printing_format = ""
    for symbol in user_entry:
        char = 0
        for c in user_entry:
            char += symbol == c
        if char >= count:
            if char == count:
                if symbol in top:
                    continue
                top += symbol
            else:
                top = symbol
            count = char
    for t in top:
        if printing_format is "":
            printing_format += t
            continue
        printing_format += ", " + t
    print("The most frequently occurring symbol(s): {} ".format(printing_format))


main()
