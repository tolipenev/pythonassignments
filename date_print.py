# Date Printer
# Converting date from one format to another
# Anatoli Penev
# 11.01.2018


def main():
    date = input('Enter a date in the form mm/dd/yyyy: ')
    print_date(date)


def print_date(date):
    month, day, year = date.split("/")
    try:
        print("The date is: {} {} {}".format(get_month_name(month), day, year))
    except KeyError as error:
        print("Month {} doesn't exist!".format(error))
        main()


def get_month_name(month):
    months = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    return months[month]


main()
