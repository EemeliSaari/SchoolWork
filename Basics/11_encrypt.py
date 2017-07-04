# Purpose: learn how to use string in depth


def upcheck(alphabet):
    if alphabet == alphabet.upper():
        return True
    else:
        return False


def encrypt(alphabet):
    REGULAR_CHARS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
                     "x", "y", "z"]

    ENCRYPTED_CHARS = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                       "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if alphabet.lower() in REGULAR_CHARS:
        index = REGULAR_CHARS.index(alphabet.lower())

        if upcheck(alphabet):
            alphabet = ENCRYPTED_CHARS[index].upper()

        else:
            alphabet = ENCRYPTED_CHARS[index]

    return alphabet


def row_encryption(string):
    new_string = ""

    for letter in string:
        new_string += encrypt(letter)

    return new_string


def read_message(text):
    new_text = []
    for sentence in text:
        new_text.append(row_encryption(sentence))

    return new_text


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    i = 1
    message = []

    while i > 0:

        text = input()
        if text != "":
            message.append(text)
            i += 1
        else:
            i *= 0

    print("ROT13:")

    encrypted = read_message(message)

    for text in encrypted:
        print(text)


main()
