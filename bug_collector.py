# Automobile costs
# Calculation of costs
# Anatoli Penev
# 09.12.2017


# Main function

def main():
    # Call an intro function so the user doesn't have to
    # press Enter to start the function.
    intro()

    # Initialize an accumulator variable.
    bugs_collected = 0.0

    # Ask the user to enter the number of bugs collected for each
    # of the 7 days.
    for counter in range(7):
        daily = float(input('Enter the number of bugs collected daily: '))
        bugs_collected = bugs_collected + daily

    # Display the total bugs collected.
    print('The total number of bugs collected over 7 days was', format(bugs_collected, ',.2f'))


def intro():
    # Explain what we are doing.
    print('This program calculates the sum of')
    print('the number of bugs collected over')
    print('a 7 day period.')


# Call the main function.
main()