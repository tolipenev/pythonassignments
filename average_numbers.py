# Average Numbers
# Python program for calculation of average numbers in file
# Anatoli Penev
# 27.12.1017


def main():
    numbers_file = 'numbers.txt'
    total, count = calc_total_and_count_numbers(numbers_file)
    print("Average of numbers in {} is {}.".format(numbers_file, total / count))


def calc_total_and_count_numbers(filename):
    try:
        total = 0
        numbers_count = 0
        numbers_file = open(filename, 'r')
        for line in numbers_file:
            total += int(line)
            numbers_count += 1
    except IOError as e:
        print("Input/Output error while handling {}: {}".format(filename, e))
    except ValueError as e:
        print("Error converting line to integer: {}".format(e))
    finally:
        numbers_file.close()
    return total, numbers_count


main()
