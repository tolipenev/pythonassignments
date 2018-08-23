# Tip, tax and total
# Calculation of amount for a meal purchased in a restaurant
# Anatoli Penev
# 19.11.2017

food_charge = float(input("Money spent on food: "))  # How much money was spent on the food
tip = 0.15  # Percentage for the tip left
sales_tax = 0.07  # Percentage for tax for meal
tip_left = tip*food_charge  # Tip left
tax_left = sales_tax*food_charge  # Tax calculated
total_spent = food_charge+tip_left+tax_left  # Total amount spent

print("Amount spent for meal = ", format(food_charge, ',.2f'))  # Show how much was spent for meal
print("Tip left for restaurant = ", format(tip_left, ',.2f'))  # Tip left by customer
print("Tax from restaurant = ", format(tax_left, ',.2f'))  # Tax from restaurant
print("Total amount spent including tax and tip = ", format(total_spent, ',.2f'))  # Total spent with tax and tip
