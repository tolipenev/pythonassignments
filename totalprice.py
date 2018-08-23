# Total purchase
# Calculate and show the total purchase for items
# Anatoli Penev
# 27.10.1017

mouse = float(input('Enter price'))  # enter price for item "mouse"
keyboard = float(input('Enter price'))  # enter price for item "keyboard"
desk = float(input('Enter price'))  # enter price for item "desk"
chair = float(input('Enter price'))  # enter price for item "chair"
monitor = float(input('Enter price'))  # enter price for item "monitor"
tax = 0.06  # tax amount
tax_price = (mouse+keyboard+desk+chair+monitor)*tax  # math calculation for total price for all items purchased
subtotal = (mouse+keyboard+desk+chair+monitor)  # subtotal price
tax_price_added = tax_price+subtotal
print('Tax amount is', tax)  # Show tax amount
print('Total price before tax', subtotal)  # Total before tax
print('Total amount of items purchased is', tax_price)  # Total price after tax
print('Subtotal + Tax', tax_price_added)  # subtotal + tax added
