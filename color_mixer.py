# Color Mixer
# Mix colors from the main spectrum colors
# Anatoli Penev
# 30.11.2017


def main():
    color1 = input("Enter a color from red, blue or yellow: ")
    color2 = input("Enter another color from red, blue or yellow: ")
    mix(color1, color2)


def mix(color1, color2):
    if color1 == 'red' and color2 == 'yellow' or \
            color1 == 'yellow' and color2 == 'red':
        print('Orange')
    elif color1 == 'blue' and color2 == 'yellow' or \
            color1 == 'yellow' and color2 == 'blue':
        print('Green')
    elif color1 == 'blue' and color2 == 'red' or \
            color1 == 'red' and color2 == 'blue':
        print('Purple')
    else:
        print('Error')


main()
