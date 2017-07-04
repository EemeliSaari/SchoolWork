# Purpose: lean how to use list data structure which contains string


def better_split(list_variable):
    """
    Adds space between every index in a list
    :param list_variable:
    :return:
    """
    new_list = []

    for word in list_variable:
        new_list.append(word)
        new_list.append(" ")

    new_list.pop(len(new_list)-1)

    return new_list


def list_filler(row_variable,spaces_value):
    """
    Adds extra spaces to fill each row
    :param row_variable: list of string
    :param spaces_value: number of spaces required
    :return: complete printable row
    """
    spaces = spaces_value
    new_row = row_variable

    while spaces > 0:
        i = 0
        while i < len(new_row):
            if " " in new_row[i]:
                new_row[i] += " "
                spaces -= 1

            if spaces == 0:
                i += len(new_row)
            else:
                i += 1

    return new_row


def join_list(list_var):
    """
    Converts a list of string into a single list
    :param list_var: list of multiple lists
    :return: list of string
    """
    whole_text = ""

    for row in list_var:
        whole_text += row + " "

    whole_list = better_split(whole_text.split(" "))

    return whole_list


def list_counter(list_variable):
    """
    Counts the length of list
    :param list_variable: list of string
    :return: length as integer
    """
    if list_variable:

        length = 0
        for var in list_variable:
            length += len(var)
        return length

    else:
        return 0


def list_to_string(list_var):
    """
    Converts a list into a single string
    :param list_var: list of string
    :return: printable text
    """
    string_var = ""
    for text in list_var:
        string_var += text

    return string_var


def parser(whole_list,row_len):
    """
    Parses through the users text
    :param whole_list: whole text as a list
    :param row_len: maximum characters for each row
    :return: parsed text as a list
    """
    old_list = whole_list
    new_list = []

    while len(old_list) > 0:
        i = 1
        new_row = []

        while i > 0:

            if list_counter(new_row) // row_len < 1:
                if len(old_list) > 0:
                    new_row.append(old_list[0])
                    old_list.pop(0)
                else:
                    new_list.append(new_row)
                    break
            else:
                if list_counter(new_row) < row_len:

                    if new_row[len(new_row)-1] == " ":
                        new_row.pop(len(new_row) - 1)
                    else:
                        old_list.insert(0,new_row[len(new_row)-1])
                        new_row.pop(len(new_row) - 1)

                    new_list.append(new_row)
                else:
                    if new_row[len(new_row)-1] == " ":
                        new_row.pop(len(new_row)-1)
                        new_list.append(new_row)

                    else:
                        if list_counter(new_row) == row_len:
                            new_list.append(new_row)
                        else:
                            old_list.insert(0, new_row[len(new_row) - 1])
                            new_row.pop(len(new_row) - 1)

                            if new_row[len(new_row)-1] == " ":
                                new_row.pop(len(new_row) - 1)

                            new_list.append(new_row)
                i *= 0

        if len(old_list) > 0:
            if old_list[0] == " ":
                old_list.pop(0)

    for i in range(0,len(new_list)-1):
        new_list[i] = list_filler(new_list[i],row_len % list_counter(new_list[i]))

    return new_list


def main():

    print("Enter text rows. Quit by entering an empty row.")

    i = 1
    text = []

    while i > 0:

        row = input()
        if row != "":
            text.append(row)
            i += 1
        else:
            i *= 0

    characters = int(input("Enter the number of characters per line: "))
    leveled_text = parser(join_list(text), characters)

    for row in leveled_text:
        print(list_to_string(row))

main()