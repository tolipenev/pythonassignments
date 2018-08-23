# Insurance
# Insurance costs
# Anatoli Penev
# 26.11.2017


# The main function
def main():
    cost = float(input("Enter the property cost to be insured:  ", ))
    insurance(cost)


# Insurance function for calculation
def insurance(conversion):
    percentage = 0.8  # multiplier used in formula
    min_insurance = conversion * percentage
    print("Minimum insurance costs =", format(min_insurance, ',.2f'))


# Call main
main()
