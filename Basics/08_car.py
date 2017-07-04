# TIE-02100
# Purpose: learn more advanced geometry calculus and how to use
#           functions in depth
from math import sqrt


def menu():
    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    MENU_TEXT = "1) Fill 2) Drive 3) Quit \n-> "

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input(MENU_TEXT)

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x,y,new_x,new_y,gas,gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


# This function has three parameters which are all FLOATs:
#       (1) the size of the tank
#       (2) the amount of gas that is requested to be filled in
#       (3) the amount of gas in the tank currently

# The parameters have to be in this order.
# The function returns one FLOAT that is the amount of gas in the
# tank AFTER the filling up.
def fill(tank_size,tank_fill,tank_current):

    if tank_fill > tank_size:
        return tank_size

    else:
        remaining = tank_current + tank_fill

        if remaining > tank_size:
            return tank_size

        else:
            return remaining


# This function has six parameters. They are all floats.
#   (1) The current x coordinate
#   (2) The current y coordinate
#   (3) The destination x coordinate
#   (4) The destination y coordinate
#   (5) The amount of gas in the tank currently
#   (6) The consumption of gas per 100 km of the car

# The function returns three floats:
#   (1) The amount of gas in the tank AFTER the driving
#   (2) The reached (new) x coordinate
#   (3) The reached (new) y coordinate
def drive(current_x,current_y,destination_x,destination_y,current_tank,consumption):

    if current_tank != 0:
        if current_x != destination_x:                  # Checks if we are only on x-axis
            if current_y != destination_y:              # Checks if we are only on y-axis
                m = journey_calc(current_x, destination_x, current_y, destination_y)
                var3 = can_we_make_it(m, consumption, current_tank)
                if var3 >= 0:
                    return var3, destination_x, destination_y

                else:
                    p = (100 * current_tank) / consumption
                    ratio = p / m

                    new_x = ratio * (destination_x - current_x) + current_y
                    new_y = ratio * (destination_y - current_y) + current_y
                    remaining_tank = 0

                    return remaining_tank, new_x, new_y
            else:
                journey = destination_x - current_x
                var2 = can_we_make_it(journey, consumption, current_tank)
                if var2 >= 0:
                    return var2, destination_x, destination_y

                else:
                    new_x = (100 * current_tank) / consumption + current_x
                    remaining_tank = 0
                    return remaining_tank, new_x, destination_y
        else:

            journey = destination_y - current_y
            var1 = can_we_make_it(journey, consumption, current_tank)
            if var1 >= 0:
                return var1, destination_x, destination_y

            else:
                new_y = (100 * current_tank) / consumption + current_y
                remaining_tank = 0
                return remaining_tank, destination_x, new_y

    else:
        return current_tank, current_x, current_y


# Calculates the sideways distance from a to b.
def journey_calc(x1,x2,y1,y2,):
    a = x2 - x1
    b = y2 - y1

    c = sqrt(a * a + b * b)

    return c


# Tests if the distance can be travelled with the current fuel.
def can_we_make_it(trip,consumption,current):
    required = (abs(trip) * consumption) / 100
    remaining = current - required

    return remaining


def read_number(prompt, error_message="Incorrect input!"):
    # This function reads input from the user.
    # Do not touch this function.
    try:
        return float(input(prompt))
    except ValueError as e:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


main()
