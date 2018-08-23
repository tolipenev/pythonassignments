# Feet to inches
# Conversion formula
# Anatoli Penev
# 15.12.1017


# Main function
def main():
    # Ask the user for the number of feet to be converted to inches.
    feet = float(input('Enter the number of feet you would like converted to inches: '))

    # Convert feet to inches
    inches = feet_to_inches(feet)
    # Print inches
    print("There are", format(inches, ',.2f'), "inches", "in", format(feet, ',.2f'), "feet")


# Write a function that converts feet to inches.
def feet_to_inches(feet):
    return 12.0 * feet


# Call the main function.
main()
