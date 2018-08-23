# Mass and Weight
# Calculate newtons from kilograms
# Anatoli Penev
# 30.11.2017


# Main function
# Ask the user to enter an object's mass.
def main():
    mass = float(input("Enter an object's mass in kilograms: "))
    scale(mass)


# Calculate the weight in newtons (weight=mass*9.8)
def scale(mass):
    weight = mass * 9.8
    if weight >= 1000:
        print('The object is too heavy.')
    elif weight <= 10:
        print('The object is too light.')
    else:
        print('The corresponding weight in newtons is ', weight, 'newtons.')


# Call the main function.
main()
