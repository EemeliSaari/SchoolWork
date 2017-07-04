# Purpose: learn how to combine different data structures such as
#           list and dict


def sort_neglecting_case(data_variable):
    """
    Sorts data structure ignoring ASCII-value
    :param data_variable: list/dict of string positions/keys
    :return: sorted list
    """
    return sorted(data_variable, key=lambda var: var.lower())


def highest(dict_variable):
    """
    Checks the highest key value from dict
    :param dict_variable: dict structure from total_sum
    :return: list containing the shops and the total price
    """
    new_list = []
    sorted_dict = {}
    for var in dict_variable:

        if dict_variable[var] in sorted_dict:
            sorted_dict[dict_variable[var]].append(var)
        else:
            sorted_dict[dict_variable[var]] = [var]

    temp_list = []
    for value in sorted(sorted_dict):
        temp_list.append(value)

    if len(temp_list) > 1:
        for i in range(1,len(temp_list)):
            if temp_list[i] != temp_list[i-1]:
                sorted_dict.pop(temp_list[i])

    for value in sorted_dict:
        new_list.append([sorted_dict[value],value])

    return new_list


def total_sum(list_variable):
    """
    Adds all the list numbers into single value
    :param list_variable:list of numbers
    :return: total value
    """

    cost = 0

    for value in list_variable:
        cost += value[1]

    return cost


def product_price(list_of_items,dict_variable):
    """
    Checks each shopping bags price for every shop
    :param list_of_items: list of items
    :param dict_variable: dict of the shops and available items
    :return: data containing the shop and their price
    """

    new_dict = {}

    for shops in dict_variable:
        new_list = []

        for items in dict_variable[shops]:

            for item in list_of_items:
                if item in items:
                    new_list.append(items)

        if len(list_of_items) == len(new_list):
            new_dict[shops] = total_sum(new_list)

    return new_dict


def list_sorter(dict_variable):
    """
    Checks all the available products in all the stores
    :param dict_variable: dict of the shops and available items
    :return: product and products price
    """

    new_dict = {}

    for shops in dict_variable:

        for item in dict_variable[shops]:

            if item[0] in new_dict:

                if item[1] < new_dict[item[0]]:

                    new_dict[item[0]] = item[1]

            else:
                new_dict[item[0]] = item[1]

    return new_dict


def read_file(file_name):
    """
    Reads a file and saves it into dict structure of lists
    :param file_name: file that we use as data
    :return: dict and False if Error occurred
    """

    try:
        file = open(file_name,"r")
        data = {}

        for line in file:

            parts = line.split(":")

            if parts[0] in data:
                data[parts[0]].append([parts[1],float(parts[2])])
            else:
                data[parts[0]] = [[parts[1],float(parts[2])]]

        return data
    except IndexError:
        return False
    except FileNotFoundError:
        return False
    except ValueError:
        return False


def main():
    """
    UI to operate the shopping bag
    :return:
    """

    items = read_file("tuotetiedot.txt")

    if items:
        print("Tervetuloa kauppakorisovellukseen!\n"
              "Käytettävissä olevat komennot:\n"
              " T ulosta kaupat tuotteineen\n"
              " S aatavilla olevien tuotteiden listaus\n"
              " K auppakorin halvin myyjä\n"
              " Q uit\n")

        syöte = ""
        while syöte != "Q":
            syöte = input("\nAnna komento (T, S, K, Q): ").upper()

            if syöte == "T":

                for shop in sorted(items):
                    print(shop)

                    for item in sorted(items[shop]):
                        print("    {:<15s} {:>10.2f} e".format(item[0],item[1]))

            elif syöte == "S":
                all_items = list_sorter(items)

                print("Saatavilla olevat eri tuotteet:")
                for product in sort_neglecting_case(all_items):
                    print("    {:<15s} {:>10.2f} e".format(product, all_items[product]))

            elif syöte == "K":
                lines = input("Anna tuotteet eroteltuna välilyönneillä:\n")
                parts = lines.split(" ")
                result = highest(product_price(parts,items))

                if len(result) > 0:         # If shops sold any of the items
                    if len(result[0][0]) > 1:
                        s = ", "
                        print("Seuraavat kaupat myyvät yhtä halvalla {:.2f} e hinnalla: {}"
                              .format(result[0][1],s.join(sorted(result[0][0]))))

                    if len(result[0][0]) == 1:
                        print("Halvin kauppa tälle korille on {} {:.2f} e hinnallaan!"
                              .format(result[0][0][0],result[0][1]))

                else:
                    print("Yksikään kauppa ei myy kaikkia kauppakorin tuotteita!")

            elif syöte == "Q":
                print("Hei hei!")
                return

            else:
                print("Virheellinen komento!")

    else:
        print("Tiedostoa luettaessa tapahtui virhe!")

main()
