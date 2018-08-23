# Area of Rectangles
# Length and wight of two rectangles
# Anatoli Penev
# 30.11.2017


def main():
    rect_a_l = float(input("Enter the length of the rectangle "))
    rect_a_w = float(input("Enter the wight of the rectangle "))
    rect_b_l = float(input("Enter the length of the rectangle "))
    rect_b_w = float(input("Enter the wight of the rectangle "))
    area_a = rect_a_l * rect_a_w
    area_b = rect_b_l * rect_b_w
    print("Total area of rectangle A is ", format(area_a, ',.2f'))
    print("Total area of rectangle B is ", format(area_b, ',.2f'))
    calc(area_a, area_b)


def calc(area_a, area_b):
    if area_a > area_b:
        print('Rectangle A has the greater area.')
    elif area_b > area_a:
        print('Rectangle B has the greater area.')
    else:
        print('Rectangle A and B has the same area.')


main()
