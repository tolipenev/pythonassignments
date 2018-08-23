# Kilometers Converter
# Program to convert distance
# Anatoli Penev
# 26.11.2017


# The main function for calculating
def main():
    kilometers = float(input("Enter the kilometers to be converted:  ", ))
    miles(kilometers)


# Miles functions gives
# the formula used for conversion
def miles(conversion):
    multiplier = 0.6214  # multiplier used in formula
    miles = conversion * multiplier
    print("Distance in miles =", format(miles, ',.2f'))


# Call main
main()
