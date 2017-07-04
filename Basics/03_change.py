# Purpose: learn how to use basic operations in python


def main():
    # Calculates the change given back for given purchase

    price = int(input("Purchase price: "))
    payment = int(input("Paid amount of money: "))

    ten = (payment - price) // 10
    five = ((payment - price) % 10) // 5
    two = (((payment - price) % 10) % 5) // 2
    one = ((((payment - price) % 10) % 5) % 2)

    if payment > price:
        print("Offer change:")

        if ten > 0:
            print(ten, "ten-euro notes")

        if five > 0 :
            print(five, "five-euro notes")

        if two > 0:
            print(two, "two-euro coins")

        if one > 0:
            print(one, "one-euro coins")

    else:
        print("No change")

main()