import random
import sys

BLANK = "  "

def main():
    print("""
    Use the WASD keys to move the tiles
back into their original order:
    1  2  3  4
    5  6  7  8
    9 10 11 12
    13 14 15
    """)
    input("Enter to start")

    puzzle = random_puzzle()
    display_puzzle(puzzle)

    while True:
        response = ask_player_move(puzzle)
        make_move(puzzle, response)
        display_puzzle(puzzle)

        if puzzle == generate_new_puzzle():
            print("You Win!")
            sys.exit()

def make_move(puzzle, response):
    blank_x, blank_y = find_blank_spaces(puzzle)
    if response == "W":
        puzzle[blank_x][blank_y], puzzle[blank_x][blank_y - 1] = puzzle[blank_x][blank_y - 1], puzzle[blank_x][blank_y]
    elif response == "A":
        puzzle[blank_x][blank_y], puzzle[blank_x - 1][blank_y] = puzzle[blank_x - 1][blank_y], puzzle[blank_x][blank_y]
    elif response == "S":
        puzzle[blank_x][blank_y], puzzle[blank_x][blank_y + 1] = puzzle[blank_x][blank_y + 1], puzzle[blank_x][blank_y]
    elif response == "D":
        puzzle[blank_x][blank_y], puzzle[blank_x + 1][blank_y] = puzzle[blank_x + 1][blank_y], puzzle[blank_x][blank_y]


def ask_player_move(puzzle):
    while True:
        blank_x, blank_y = find_blank_spaces(puzzle)
        if blank_y != 3:
            s = "S"
        else:
            s = " "
        if blank_x != 3:
            d = "D"
        else:
            d = " "
        if blank_y != 0:
            w = "W"
        else:
            w = " "
        if blank_x != 0:
            a = "A"
        else:
            a = " "
        print(f"available moves: [{w}], [{a}], [{s}], [{d}]")
        print("type: [QUIT] to exit the game")
        response = input("> ").upper()
        if response == "QUIT":
            sys.exit()
        if response in (w + a + s + d).replace(" ", ""):
            return response


def generate_new_puzzle():
    """Return a list of list that represents a new tile puzzle"""
    return [[" 1", " 5", " 9", "13"],
            [" 2", " 6", "10", "14"],
            [" 3", " 7", "11", "15"],
            [" 4", " 8", "12", BLANK]]

def display_puzzle(puzzle):
    board = f"""
+------+------+------+------+
|      |      |      |      |
| {puzzle[0][0]}   | {puzzle[1][0]}   | {puzzle[2][0]}   |  {puzzle[3][0]}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {puzzle[0][1]}  |  {puzzle[1][1]}  |  {puzzle[2][1]}  |  {puzzle[3][1]}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {puzzle[0][2]}  |  {puzzle[1][2]}  |  {puzzle[2][2]}  |  {puzzle[3][2]}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {puzzle[0][3]}  |  {puzzle[1][3]}  |  {puzzle[2][3]}  |  {puzzle[3][3]}  |
|      |      |      |      |
+------+------+------+------+
"""
    print(board)


def random_puzzle():
    puzzle = generate_new_puzzle()
    for i in range(200):
        # find blank space
        blank_x, blank_y = find_blank_spaces(puzzle)
        move = []

        if blank_y != 3:
            move.append("S")
        if blank_x != 3:
            move.append("D")

        if blank_y != 0:
            move.append("W")
        if blank_x != 0:
            move.append("A")

        #print(move)
        random_move = random.choice(move)
        #print(f" before random move: {random_move} blank_x: {blank_x} blank_y: {blank_y}")
        #display_puzzle(puzzle)

        #move blank spaces
        if random_move == "W":
            puzzle[blank_x][blank_y], puzzle[blank_x][blank_y-1] = puzzle[blank_x][blank_y-1], puzzle[blank_x][blank_y]
        elif random_move == "A":
            puzzle[blank_x][blank_y], puzzle[blank_x-1][blank_y] = puzzle[blank_x-1][blank_y], puzzle[blank_x][blank_y]
        elif random_move == "S":
            puzzle[blank_x][blank_y], puzzle[blank_x][blank_y+1] = puzzle[blank_x][blank_y+1], puzzle[blank_x][blank_y]
        elif random_move == "D":
            puzzle[blank_x][blank_y], puzzle[blank_x+1][blank_y] = puzzle[blank_x+1][blank_y], puzzle[blank_x][blank_y]

        blank_x, blank_y = find_blank_spaces(puzzle)
        #print(f" after random move: {random_move} blank_x: {blank_x} blank_y: {blank_y}")
        #display_puzzle(puzzle)
        #print()

    return puzzle

def find_blank_spaces(puzzle):
    for x in range(4):
        for y in range(4):
            if puzzle[x][y] == BLANK:
                return x, y

if __name__ == '__main__':
    main()