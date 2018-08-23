# Random Number File reader
# Python program for reading numbers in a file
# Anatoli Penev
# 06.01.2018


def main():
    days = 7
    sales = [0] * days
    index = 0
    print("Enter the sales for each day")
    while index < days:
        print("Day #", index + 1, ": ", sep="", end="")
        sales[index] = float(input())
        index += 1

    print('Here are the values you entered:')
    for value in sales:
        print(value)


def calculate():
    days = 7
    sales = [0] * days
    total = 0
    for i in range(7):
        sale = input('Enter a store\'s sales for today: ')
        sales.append(sale)
        total += float(sale)
    print(sales)
    print(total)


calculate()
main()
