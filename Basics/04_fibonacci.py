# Purpose: learn how to use while loop and print format


def fibonacci():
    # prints fibonacci series

    a, b, n = 0, 1, 1
    var = int(input("How many Fibonacci numbers do you want? "))

    while n <= var:

        a, b = b, a + b
        print("{:1d}".format(n),". ",a, sep="")
        n += 1

    print()

fibonacci()

