# Automobile costs
# Calculation of costs
# Anatoli Penev
# 26.11.2017


# Main function and monthly calculation
def main():
    loan_payment = float(input("Loan payment expense: ", ))
    insurance = float(input("Insurance cost: ", ))
    gas = float(input("Gas costs ", ))
    oil = float(input("Oil costs ", ))
    tires = float(input("Tires costs ", ))
    maintenance = float(input("Maintenance ", ))

    total = loan_payment + insurance + gas + oil + tires + maintenance
    calc(total)
    print("Total monthly costs =", format(total, ',.2f'))


# Calc function gives the annual cost
def calc(value):
    multiplier = 12
    annual = value * multiplier
    print("Total annual costs =", format(annual, ',.2f'))


# Call main
main()
