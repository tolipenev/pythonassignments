# Automobile costs
# Calculation of costs
# Anatoli Penev
# 09.12.2017


# Main function
def main():
    user_entry = input('How many minutes were you exercising? ')
    calories_burn(user_entry)


def calories_burn(user_entry):
    calories = 0
    for i in range(user_entry):
        calories += 3.9
    print("Burned calories =", format(user_entry, ',.2f'))


main()



