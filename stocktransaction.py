# Stock transaction
# Program for stock transaction in a period
# Anatoli Penev
# 19.11.2017

# initial purchase
shares_purchased = 1000
stock_price_per_share_bought = 32.87
payment_for_stock= shares_purchased*stock_price_per_share_bought
commission = 0.02
commission_paid = commission*payment_for_stock

# two weeks later
shares_sold = 1000
stock_price_per_share_sold = 33.92
earnings_after_sale = shares_sold*stock_price_per_share_sold
commission_paid_on_sale = commission*earnings_after_sale
total_commission_paid = commission_paid+commission_paid_on_sale
earnings = earnings_after_sale-payment_for_stock
earning_after_commissions = earnings - total_commission_paid

print("Amount paid for stock = ", payment_for_stock)
print("Amount paid to broker when buying = ", commission_paid)
print("Amount received for sold stock = ", earnings_after_sale)
print("Amount paid to broker when selling = ", commission_paid_on_sale)
print("Amount earned = ", earnings)
print("Amount earned after both commissions payed = ", earning_after_commissions)
if earning_after_commissions > 0:
    print("Joe made a profit")
else:
    print("Joe lost money")
