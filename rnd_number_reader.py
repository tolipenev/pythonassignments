# Random Number File reader
# Python program for reading numbers in a file
# Anatoli Penev
# 27.12.1017


def main():
    file_display("random_numbers.txt")


def file_display(file_to_read):
    try:
        rnd_file = open(file_to_read, "r")

        total = 0
        rnd_numbers = 0
        line = rnd_file.readline()

        while line != "":
            rnd_numbers +=1
            rnd_number = int(line)
            total += rnd_number
            print(rnd_number)
            line = rnd_file.readline()
    except Exception as error:
        print("Error: ", error)
    else:
        print("\nTotal count of numbers in file: " + str(total),
              "\nThere are", str(rnd_numbers), "numbers in the file")
        rnd_file.close()
    finally:
        print("File read successful!")


main()
