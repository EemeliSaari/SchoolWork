# Purpose: learn how to divide the code into multiple functions


def calories(list_variable):
    """
    Converts the measured steps to energy
    :param list_variable: list of steps
    :return: calories consumed as kcal
    """
    FLOAT_VALUE = steps_to_kilometers(list_variable)
    cal = int(FLOAT_VALUE * 50)

    return cal


def steps_to_kilometers(list_variable):
    """
    Converts the measured steps from list to kilometers
    :param list_variable: list of steps
    :return: Kilometers walked as float number
    """
    FLOAT_VALUE = list_to_value(list_variable)

    return FLOAT_VALUE / 2500 * 1.5


def list_to_value(list_variable):
    """
    Adds all the list values into a single value
    :param list_variable: list of steps
    :return: Added total as int number
    """

    INT_VALUE = 0
    for value in list_variable:
        INT_VALUE += value

    return INT_VALUE


def list_division(list_variable):
    """
    Splits the list for given division range
    :param list_variable:
    :return: original list values divided into different subsets
    """

    base_value = 1000
    highest_value = sorted(list_variable)[len(list_variable) - 1]
    divided_list = []

    while base_value < highest_value:
        compared = list_compare(list_variable, base_value, base_value + 4000)
        divided_list.append(compared)
        base_value += 4000

    return divided_list


def graphical_data(list_variable):
    """
    Saves the information of the list into data list
    :param list_variable: divided_list
    :return: subset of data in list format
    """
    data_list = []
    base_value = 1000
    for values in list_variable:

        data_list.append([base_value,len(values)])
        base_value += 4000

    return data_list


def graph_analyze(list_variable):
    """
    Checks which division range has the biggest value
    :param list_variable: graphical_data list
    :return: int value from the data structure
    """
    value = list_variable[0][1]
    STEPS = list_variable[0][0]

    for var in list_variable:

        if var[1] > value:
            value = var[1]
            STEPS = var[0]

    return STEPS


def list_compare(list_variable, low, high):
    """
    Selects accepted values for given range
    :param list_variable: list of int values
    :param low: lowest compared value
    :param high: highest compared value
    :return: list of accepted values
    """
    compared_list = []
    for value in list_variable:

        if low < value < high:
            compared_list.append(value)

    return compared_list


def reject(list_variable):
    """
    Rejects all underperformed measurements
    :param list_variable: list of steps
    :return: accepted values as list
    """

    accepted_list = []
    for value in list_variable:

        if value > 1000:
            accepted_list.append(value)

    return accepted_list


def line_reader():
    """
    Saves user input into list
    :return: list of int values
    """
    lines = []

    I = 1
    while I > 0:
        input_int = input()

        if input_int == "":
            I *= 0

        else:
            lines.append(int(input_int))

    return lines


def menu():
    """
    Users display of the step measurements
    Containing all the wanted information
    :return:
    """
    print("Enter the amount of steps/day, one day per line.\n"
          "End by entering an empty row.")

    data = line_reader()

    if len(data) > 0:
        print("Information related to the period of measurement ({:d} days):"
              .format(len(data)))

        data_rejected = reject(data)
        # If there's any rejected measurements
        if len(data_rejected) < len(data):
            print("Rejected {:d} results of under 1000 steps/day."
                  .format(len(data) - len(data_rejected)))
        # If there's any accepted measurements
        if len(data_rejected) > 0:
            print()
            print("Graphical representation of information:")

            display = graphical_data(list_division(data_rejected))

            for var in display:
                print("{:5} {:s}"
                      .format(var[0],var[1] * "#"))
            print()

            HIGHEST_VALUE = sorted(data_rejected)[len(data_rejected) - 1]

            # Division range with the highest number of values
            A = graph_analyze(display)
            B = A + 4000

            print("Steps taken during most of the days:"
                  " over {:d} but under {:d} steps"
                  .format(A,B))

            print("Days with over 9000 steps taken: {:d} days"
                  .format(len(list_compare(data_rejected,9000,HIGHEST_VALUE+1))))

            print("Longest distance walked during a day: {:.02f} km"
                  .format(steps_to_kilometers([HIGHEST_VALUE])))

            print("Total calories consumed by walking: {:d} kcal"
                  .format(calories(data_rejected)))


def main():
    menu()


main()
