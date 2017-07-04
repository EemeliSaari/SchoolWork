# Purpose: learn how to use basic basic text based user interface
#           combined with basic geometry calculus

import math


def circle(r):
    """
    Basic calculator for circle
    :param r: r as radius of the circle
    :return: area, circumference
    """
    circle_value = math.pi * r * r
    circle_circumference = 2 * math.pi * r

    return round(circle_value,2), round(circle_circumference,2)


def rectangle(a,b):
    """
    Basic calculator for rectangle
    :param a: side 1
    :param b: side 2
    :return: circumference, area
    """
    rectangle_area = a * b
    rectangle_circumference = 2 * (a + b)

    return round(rectangle_circumference,2), round(rectangle_area,2)


def square(a):
    """
    Basic calculator for square
    :param a: length of one side
    :return: area, circumference
    """
    area_value = a * a
    area_circumference = a * 4
    return area_value, area_circumference


def menu():
    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            var_square = 1

            while var_square > 0:
                square_question = float(input("Enter the length of the square's side: "))

                if square_question <= 0:
                    var_square += 1

                else:
                    var_square *= 0
                    value1 = square(square_question)
                    print("The total circumference is {:.2f}".format(value1[1]))
                    print("The surface area is {:.2f}".format(value1[0]))

        elif answer == "r":
            var1_rectangle = 1
            var2_rectangle = 1
            var1_general = 0
            while var1_general < 2:
                rectangle_question1 = float(input("Enter the length of the rectangle's side 1: "))

                if rectangle_question1 <= 0:
                    var1_rectangle += 1

                else:
                    while var2_rectangle > 0:
                        var1_general += 1
                        rectangle_question2 = float(input("Enter the length of the rectangle's side 2: "))

                        if rectangle_question2 <= 0:
                            var2_rectangle += 1

                        else:
                            var1_general += 1
                            var2_rectangle *= 0
                            value2 = rectangle(rectangle_question1,rectangle_question2)
                            print("The total circumference is {:.2f}".format(value2[0]))
                            print("The surface area is {:.2f}".format(value2[1]))

        elif answer == "q":
            return

        elif answer == "c":
            var_circle = 1

            while var_circle > 0:
                circle_question = float(input("Enter the circle's radius: "))

                if circle_question <= 0:
                    var_circle += 1

                else:
                    var_circle *= 0
                    value3 = circle(circle_question)
                    print("The total circumference is {:.2f}".format(value3[1]))
                    print("The surface area is {:.2f}".format(value3[0]))

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


main()