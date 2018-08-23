# Sales tax
# Computing the sale with taxes added
# Anatoli Penev
# 26.11.2017


# Main function
def main():
    price = float(input("Enter the amount of purchase "))
    calctax(price)


# Calculation function and constants
def calctax(price):
    state_tax = 0.04
    county_tax = 0.02
    state_sale = price * state_tax
    county_sale = price * county_tax
    total_tax = county_tax + state_tax
    total_sale = price + total_tax
    print("Amount of purchase = ", format(price, ',.2f'), "\n",
          "State tax = ", format(state_tax, ',.2f'), "\n",
          "County tax =", format(county_tax, ',.2f'), "\n",
          "State sale with tax= ", format(state_sale, ',.2f'), "\n",
          "County sale with tax=", format(county_sale, ',.2f'), "\n",
          "Total sale tax =", format(total_tax, ',.2f'), "\n",
          "Total of sale = ", format(total_sale, ',.2f'), "\n")


main()
