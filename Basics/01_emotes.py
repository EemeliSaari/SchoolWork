# Purpose: learn the basic boolean in Python


def main():
    # Simple emote generator based on your current mood

    line = input("How do you feel? (1-10) ")
    feeling = float(line)
    if 0 < feeling <= 10:
        if 10 > feeling > 7:
            smiley = ":-)"
        elif 1 < feeling < 4:
            smiley = ":-("
        elif feeling == 1:
            smiley = ":'("
        elif feeling == 10:
            smiley = ":-D"
        else:
            smiley = ":-|"
        print("A suitable smiley would be", smiley)
    else:
        print("Bad input!")

main()