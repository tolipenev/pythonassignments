# Random Number File writer
# Python program for writing random numbers in a file
# Anatoli Penev
# 27.12.1017


def main():
    rnd_file()
    generate_random_number()


def generate_random_number():
        import random
        rnd_number = random.randint(1, 100)
        return rnd_number


def rnd_file():
    try:
        rnd_numbers = int(input("How many numbers can the file hold ?: "))
        with open("random_numbers.txt", "w") as file_created:
            for rnd_number_count in range(1, rnd_numbers + 1):
                rnd_number = generate_random_number()
                file_created.write(str(rnd_number) + "\n")
            print(rnd_numbers, "numbers have been added to the file random_numbers.txt")
        print("\nFile created successfully!")
    except Exception as error:
        print("An error has occurred", error)


main()