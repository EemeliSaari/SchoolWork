# TIE-02106 Introduction to Programming
# Purpose: learn to use lists within list data structure


def ui(matrix):
    """
    Prints the game board
    :param matrix: matrix data structure
    """
    for row in matrix:
        print(row[0]+row[1]+row[2])


def row_comp(list_variable):
    """
    Checks if there's player input in the list
    :param list_variable:
    :return: True if only player inputs, False otherwise
    """
    var = 0
    for i in range(0,2):
        if list_variable[i] == ".":
            var += 1
    if var == 0:
        return True
    else:
        return False


def game(matrix,x,y):
    """
    Checks if the game continues or not
    :param matrix: game board containing 3 rows
    :param x: current row
    :param y: current column
    :return: True if game continues, otherwise False
    """
    i = 0

    if matrix[y][0] == matrix[y][1] == matrix[y][2]:
        if row_comp(matrix[y]):
            i += 1
    elif matrix[0][x] == matrix[1][x] == matrix[2][x]:
        if row_comp([matrix[0][x],matrix[1][x],matrix[2][x]]):
            i += 1
    elif matrix[0][0] == matrix[1][1] == matrix[2][2]:
        if row_comp([matrix[0][0],matrix[1][1],matrix[2][2]]):
            i += 1
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if row_comp([matrix[0][2],matrix[1][1],matrix[2][0]]):
            i += 1

    if i > 0:
        return False
    else:
        return True


def main():

    # Data structure of the playing board
    row1 = [".",".","."]
    row2 = [".",".","."]
    row3 = [".",".","."]
    board = [row1,row2,row3]

    ui(board)

    turns = 0  # How many turns have been played

    # The game continues until the board is full.
    # 9 marks have been placed on the board when the player has been
    # switched 8 times.

    while turns < 9:

        # Change the mark for the player
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            if board[y][x] == ".":
                board[y][x] = mark
                ui(board)

                if game(board, x, y):
                    turns += 1
                else:
                    print("The game ended, the winner is", mark)
                    break
            else:
                print("Error: a mark has already been placed on this square.")

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")

    else:
        print("Draw!")
main()
