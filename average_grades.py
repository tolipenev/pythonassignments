# Average grades
# Result based on grades
# Anatoli Penev
# 15.12.1017


def main():
    a = int(input('Enter a score for test A: '))
    b = int(input('Enter a score for test B: '))
    c = int(input('Enter a score for test C: '))
    d = int(input('Enter a score for test D: '))
    e = int(input('Enter a score for test E: '))
    average = calc_average(a, b, c, d, e)
    determine_grade(a, b, c, d, e)
    print('The average of your scores is', average)


def calc_average(a, b, c, d, e):

    average = (a + b + c + d + e) / 5
    return average


def determine_grade(a, b, c, d, e):
    for i in a, b, c, d, e:
        if 90 <= i:
            print('The grade of', i, 'is A')
        elif 80 <= i <= 89:
            print('The grade of', i, 'is B')
        elif 70 <= i <= 79:
            print('The grade of', i, 'is C')
        elif 60 <= i <= 69:
            print('The grade of', i, 'is D')
        elif i < 60:
            print('The grade of', i, 'is E')


main()

