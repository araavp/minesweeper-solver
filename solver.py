# Minesweeper Solver
# For expert mode on minesweeperonline.com
# 16 x 30 board with 99 mines
"""
1-8 are number of surrounding bombs
9 is empty square
b stands for bomb
c stands for next space for user to choose
"""

board_height = 16
board_width = 30
board = [[9 for x in range(board_width)] for y in range(board_height)]
total_mines = 99
count = 0
nonzero_heights = []
nonzero_widths = []
ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos = None, None, None, None, None, None, None, None
positions = [ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos]
number = 0
number_input = ""
u_input = ""
user_quit = ""
more_input = ""
height = 0
width = 0


def start(mine_board):
    show_board(mine_board)
    user_input(mine_board)
    print("reached here")
    show_board(mine_board)
    print("reached here part 2")
    find_nonzero(mine_board)
    show_board(mine_board)


def show_board(mine_board):
    for i in range(len(mine_board)):
        print(*mine_board[i], sep=',')
    print()


def user_input(mine_board):
    global number, u_input, user_quit, number_input, height, width
    print("You can press q to quit at anytime")
    while True:
        try:
            height = int(input("Enter row number: ")) - 1
            if height > (len(mine_board) - 1) or height == -1:
                print("Enter a number only from 1-16")
                height = int(input("Enter row number: ")) - 1

            width = int(input("Enter column number: ")) - 1
            if width > (len(mine_board[0]) - 1) or width == -1:
                print("Enter a number only from 1-30")
                width = int(input("Enter column number: ")) - 1

            number_input = input("What is the number or bomb at that location? If it is a bomb type b: ")
            if number_input != 'b':
                number = int(number_input)
                if number > 9:
                    print("Enter a number only from 0-8 or 9 to reset that square")
                    number = int(input("What is the number at that location: "))
                mine_board[height][width] = number
            elif number_input == 'b':
                mine_board[height][width] = number_input

        except ValueError:
            user_quit = input("Press u to add more user input, c to continue, or q to quit program")
            if user_quit == 'u':
                continue
            elif user_quit == 'c':
                break
            elif user_quit == 'q':
                exit()


def c_user_input(mine_board):
    global number, u_input, user_quit, more_input
    check = 0
    for i in range(len(mine_board)):
        for j in range(len(mine_board[0])):
            if mine_board[i][j] == "c":
                check += 1
                print("You can click on the box at row: ", i+1, "and col: ", j+1, " or type q to quit")
                u_input = input("What number does it show: ")
                if u_input == "q":
                    user_quit = input("Are you sure you want to quit (y/n): ")
                    if user_quit == 'y':
                        exit()
                    elif user_quit == 'n':
                        u_input = input("What number does it show: ")
                number = int(u_input)
                if number > 8 or number < 0:
                    print("Please print an integer from 0-8")
                    number = int(input("What number does it show: "))
                mine_board[i][j] = number

    more_input = input("Do you have new squares to input? (y/n)")
    if more_input == 'y':
        user_input(mine_board)

    if check != 0:
        find_nonzero(mine_board)
    else:
        return


def find_nonzero(mine_board):
    global nonzero_heights, nonzero_widths
    nonzero_heights = []
    nonzero_widths = []
    for i in range(len(mine_board)):
        for j in range(len(mine_board[0])):
            if mine_board[i][j] != 9 and mine_board[i][j] != 'b':
                print(mine_board[i][j])
                nonzero_heights.append(i)
                nonzero_widths.append(j)
    if len(nonzero_heights) != 0:
        find_bombs(mine_board, nonzero_heights, nonzero_widths)
    else:
        return


def find_surrounding_empty(mine_board, row, col):
    global ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos, positions
    ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos = None, None, None, None, None, None, None, None
    if row == 0:
        if col == 0:
            r_pos = mine_board[row][col + 1]
            br_pos = mine_board[row + 1][col + 1]
            b_pos = mine_board[row + 1][col]
        elif 0 < col < 29:
            r_pos = mine_board[row][col + 1]
            br_pos = mine_board[row + 1][col + 1]
            b_pos = mine_board[row + 1][col]
            bl_pos = mine_board[row + 1][col - 1]
            l_pos = mine_board[row][col - 1]
        elif col == 29:
            ul_pos = mine_board[row - 1][col - 1]
            u_pos = mine_board[row - 1][col]
            b_pos = mine_board[row + 1][col]
            bl_pos = mine_board[row + 1][col - 1]
            l_pos = mine_board[row][col - 1]
    elif 0 < row < 15:
        if col == 0:
            u_pos = mine_board[row - 1][col]
            ur_pos = mine_board[row - 1][col + 1]
            r_pos = mine_board[row][col + 1]
            br_pos = mine_board[row + 1][col + 1]
            b_pos = mine_board[row + 1][col]
        elif 0 < col < 29:
            ul_pos = mine_board[row - 1][col - 1]
            u_pos = mine_board[row - 1][col]
            ur_pos = mine_board[row - 1][col + 1]
            r_pos = mine_board[row][col + 1]
            br_pos = mine_board[row + 1][col + 1]
            b_pos = mine_board[row + 1][col]
            bl_pos = mine_board[row + 1][col - 1]
            l_pos = mine_board[row][col - 1]
        elif col == 29:
            ul_pos = mine_board[row - 1][col - 1]
            u_pos = mine_board[row - 1][col]
            b_pos = mine_board[row + 1][col]
            bl_pos = mine_board[row + 1][col - 1]
            l_pos = mine_board[row][col - 1]
    elif row == 15:
        if col == 0:
            u_pos = mine_board[row - 1][col]
            ur_pos = mine_board[row - 1][col + 1]
            r_pos = mine_board[row][col + 1]
        elif 0 < col < 29:
            ul_pos = mine_board[row - 1][col - 1]
            u_pos = mine_board[row - 1][col]
            ur_pos = mine_board[row - 1][col + 1]
            r_pos = mine_board[row][col + 1]
            l_pos = mine_board[row][col - 1]
        elif col == 29:
            ul_pos = mine_board[row - 1][col - 1]
            u_pos = mine_board[row - 1][col]
            l_pos = mine_board[row][col - 1]

    positions = [ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos]
    return ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos, positions


def find_number_surrounding_empty(mine_board, row, col):
    global count, ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos, positions
    count = 0
    for pos in range(len(positions)):
        if positions[pos] == "b":
            count += 1
            if count == mine_board[row][col]:
                for position in range(len(positions)):
                    if positions[position] == 9:
                        positions[position] = "c"
                        computer_input(mine_board, position, positions[position], row, col)

                return ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos, positions

    for pos in range(len(positions)):
        if positions[pos] == 9:
            count += 1

    if count == mine_board[row][col]:
        for pos in range(len(positions)):
            if positions[pos] == 9:
                positions[pos] = "b"
                computer_input(mine_board, pos, positions[pos], row, col)

    return ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos, positions


def computer_input(mine_board, pos, value, row, col):
    if pos == 0:
        mine_board[row - 1][col - 1] = value
    elif pos == 1:
        mine_board[row - 1][col] = value
    elif pos == 2:
        mine_board[row - 1][col + 1] = value
    elif pos == 3:
        mine_board[row][col + 1] = value
    elif pos == 4:
        mine_board[row + 1][col + 1] = value
    elif pos == 5:
        mine_board[row + 1][col] = value
    elif pos == 6:
        mine_board[row + 1][col - 1] = value
    elif pos == 7:
        mine_board[row][col - 1] = value


def find_bombs(mine_board, height_array, width_array):
    for x in range(len(height_array)):
        find_surrounding_empty(mine_board, height_array[x], width_array[x])
        find_number_surrounding_empty(mine_board, height_array[x], width_array[x])
    show_board(mine_board)
    c_user_input(mine_board)


start(board)
