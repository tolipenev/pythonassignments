# Sales tax
# Computing the sale with taxes added
# Anatoli Penev
# 19.11.2017

price = float(input("Enter amount of purchase"))  # User entered price
state_tax = 0.04  # State tax percentage
county_tax = 0.02  # County tax percentage
state_sale = price*state_tax  # State sale with tax
county_sale = price*county_tax  # County sale with tax
total_tax = county_tax+state_tax  # Total sale tax
total_sale = price+total_tax  # Total sale

print("Amount of purchase = ", price)  # Amount of purchase by user
print("State tax = ", state_tax)  # Current state tax
print("County tax =", county_tax)  # Current county tax
print("State sale with tax= ", state_sale)  # State sales
print("County sale with tax=", county_sale)  # County sales
print("Total sale tax =", total_tax)  # Amount of total tax for sale
print("Total of sale = ", total_sale)  # Amount of total sale with total tax added
