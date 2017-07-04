# Purpose: learn how to use dict data structure


def main():

    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    s = ", "
    print(s.join(sorted(english_spanish)))

    while True:

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            
            word = input("Enter the word to be translated: ")

            if word in english_spanish:
                print(word,"in Spanish is",english_spanish[word])

            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng_word = input("Give the word to be added in English: ")
            spa_word = input("Give the word to be added in Spanish: ")

            english_spanish[eng_word] = spa_word

            print("Dictionary contents:")
            s = ", "
            print(s.join(sorted(english_spanish)))

        elif command == "R":
            del_word = input("Give the word to be removed: ")

            if del_word in english_spanish:
                del english_spanish[del_word]

            else:
                print("The word",del_word,"could not be found from the dictionary.")

        elif command == "P":
            spanish_english = {}

            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
                spanish_english[english_spanish[word]] = word

            print()
            print("Spanish-English")
            for word in sorted(spanish_english):
                print(word, spanish_english[word])

            print()

        elif command == "T":
            text_str = input("Enter the text to be translated in Spanish: ")
            text_list = text_str.split(" ")
            string = ""
            for word in text_list:
                if word in english_spanish:
                    string += english_spanish[word] + " "

                else:
                    string += word + " "
            print("The text, translated by the dictionary:")
            print(string.rstrip())

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


main()
