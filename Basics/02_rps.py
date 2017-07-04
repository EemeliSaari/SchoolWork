# Purpose: learn how to use boolean with input


def main():
    # Simple game of rock-paper-scissors for two players

    player1 = input("Player 1, enter your choice (R/P/S): ")
    player2 = input("Player 2, enter your choice (R/P/S): ")
    even_score = "It's a tie!"
    win = ""

    if player1 != player2:
        if player1 == "R" and player2 == "S":
            win = "Player 1 won!"
        elif player1 == "P" and player2 == "S":
            win = "Player 2 won!"
        elif player1 == "S" and player2 == "R":
            win = "Player 2 won!"
        elif player1 == "R" and player2 == "P":
            win = "Player 2 won!"
        elif player1 == "S" and player2 == "P":
            win = "Player 1 won!"
        elif player1 == "P" and player2 == "R":
            win = "Player 1 won!"

    else:
        win = even_score

    print(win)

main()