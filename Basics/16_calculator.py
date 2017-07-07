# TIE-02100


class Fraction:
    """ This class represents one single fraction that consists of
        numerator and denominator """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: fraction's numerator
        :param denominator: fraction's denominator
        """

        # Both numerator and denominator needs to integers 
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, other):
        return self.__numerator / self.__denominator < \
               other.__numerator / other.__denominator

    def __gt__(self, other):
        return self.__numerator / self.__denominator > \
               other.__numerator / other.__denominator

    def __str__(self):

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                      abs(self.__denominator))

    def simplify(self):
        """ Simplifies the Fraction"""
        common_divisor = greatest_common_divisor(self.__numerator, self.__denominator)

        numerator = self.__numerator // common_divisor
        denominator = self.__denominator // common_divisor

        return Fraction(numerator, denominator)

    def complement(self):
        numerator = self.__numerator
        denominator = self.__denominator

        if numerator < 0:

            if denominator < 0:
                denominator *= -1
            else:
                numerator *= -1
        else:
            denominator *= -1
        return Fraction(numerator, denominator)

    def reciprocal(self):
        numerator = self.__numerator
        denominator = self.__denominator

        return Fraction(denominator, numerator)

    def multiply(self, fraction_var):
        numerator = self.__numerator * fraction_var.__numerator
        denominator = self.__denominator * fraction_var.__denominator

        return Fraction(numerator, denominator)

    def divide(self, fraction_var):
        new_var = fraction_var.reciprocal()

        numerator = self.__numerator * new_var.__numerator
        denominator = self.__denominator * new_var.__denominator

        return Fraction(numerator, denominator)

    def add(self, fraction_var):
        num1, den1 = self.__numerator, self.__denominator
        num2, den2 = fraction_var.__numerator, fraction_var.__denominator

        numerator = num1 * den2 + num2 * den1
        denominator = den1 * den2

        return Fraction(numerator, denominator)

    def deduct(self, fraction_var):
        num1, den1 = self.__numerator, self.__denominator
        num2, den2 = fraction_var.__numerator, fraction_var.__denominator

        numerator = num1 * den2 - num2 * den1
        denominator = den1 * den2

        return Fraction(numerator, denominator)

    def return_string(self):
        """ Returns a string-presentation of the fraction in the format
        numerator/denominator """

        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""
        return "{:s}{:d}/{:d}".format(sign, abs(self.__numerator),
                                      abs(self.__denominator))


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm.
    """

    while b != 0:
        a, b = b, a % b
    return a


def read_file(file_name):
    """Reads file and if the info is in the wanted format,
       it will save into a dict, otherwise returns False"""
    dict_fractions = {}
    try:
        file = open(file_name,"r")

        for line in file:
            parts = line.split("=")
            name = parts[0]
            numbers = parts[1].split("/")

            dict_fractions[name] = Fraction(int(numbers[0]),int(numbers[1]))

        return dict_fractions

    except IndexError:
        return False
    except FileNotFoundError:
        return False
    except ValueError:
        return False


def menu():
    """Works as a user interface where you have multiple commands you can
       execute"""

    data = {}
    arithmetic = {"+":lambda m,n:m.add(n),
                  "-":lambda m,n:m.deduct(n),
                  "*":lambda m,n:m.multiply(n),
                  "/":lambda m,n:m.divide(n)}

    while True:
        input_var = input("> ")

        if input_var == "add":
            fraction = input("Enter a fraction in the form integer/integer: ")
            name = input("Enter a name: ")
            parts = fraction.split("/")
            data[name] = Fraction(int(parts[0]),int(parts[1]))

        elif input_var == "print":
            search = input("Enter a name: ")

            if search in data:
                print(search,"=",data[search])
            else:
                print("Name",search,"was not found")

        elif input_var == "list":
            for fraction in sorted(data):
                print(fraction,"=",data[fraction])

        elif input_var in arithmetic:
            first = input("1st operand: ")

            if first in data:
                second = input("2nd operand: ")
                if second in data:

                    operation = arithmetic[input_var](m=data[first],n=data[second])
                    print(data[first],input_var,
                          data[second],"=",
                          operation)
                    print("simplified",operation.simplify())
                else:
                    print("Name",second,"was not found")
            else:
                print("Name",first,"was not found")

        elif input_var == "read":
            file_name = input("Enter the name of the file: ")
            file_data = read_file(file_name)
            if file_data:

                for value in file_data:
                    data[value] = file_data[value]

            else:
                print("Error: the file cannot be read.")

        elif input_var == "quit":
            print("Bye bye!")
            return

        else:
            print("Unknown command!")


def main():
    menu()


main()