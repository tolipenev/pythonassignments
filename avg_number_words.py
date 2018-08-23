# Average number of words
# Count the number of words in a sentence in text file
# Anatoli Penev
# 11.01.2018


def main():
    file_name = input("Enter file name: ")
    parse_file(file_name)


def avg_words(num_words, line_count):
    return num_words/line_count


def parse_file(file_name):
    num_words = 0
    line_count = 0

    try:
        with open(file_name, 'r') as f:
            for line in f:
                line_count += 1
                num_words += len(line.split())
        print("Number of words: ", num_words)
        print("Number of lines: ", line_count)
        print("Average words per sentence: {:.2f}".format(avg_words(num_words, line_count)))

    except FileNotFoundError as error:
        print("File Not Found!", error)
        main()


main()

