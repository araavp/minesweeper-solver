# Minesweeper Solver
# For expert mode on minesweeperonline.com
# 16 x 30 board with 99 mines

import keyboard
import numpy as np


board_height = 16
board_width = 30
board = [[0 for x in range(board_width)] for y in range(board_height)]
total_mines = 99
count = 0
nonzero_heights = []
nonzero_widths = []
ul_pos, u_pos, ur_pos, r_pos, br_pos, b_pos, bl_pos, l_pos = 0, 0, 0, 0, 0, 0, 0, 0


def show_board(mine_board):
    print(np.matrix(board))


def user_input(mine_board):
    while True:
        try:
            height = int(input("Enter row number: ")) - 1
            if height > (len(mine_board) - 1):
                print("Enter a number only from 1-16")
                height = int(input("Enter row number: ")) - 1

            width = int(input("Enter column number: ")) - 1
            if width > (len(mine_board[0]) - 1):
                print("Enter a number only from 1-30")
                width = int(input("Enter column number: ")) - 1

            number = int(input("What is the number at that location: "))
            if number > 6:
                print("Enter a number only from 0-6")
                number = int(input("What is the number at that location: "))

            mine_board[height][width] = number
        except ValueError:
            user_quit = input("Press q to quit or c to continue")
            if user_quit == 'q':
                break
            elif user_quit == 'c':
                continue


def find_nonzero(mine_board):
    for i in range(len(mine_board)):
        for j in range(len(mine_board[0])):
            if mine_board[i][j] != 0:
                nonzero_heights.append(i)
                nonzero_widths.append(j)

    return nonzero_heights, nonzero_widths


def find_surrounding_empty(mine_board, row, column):
    try:
        return
    except IndexError:
        return None


"""
for x in range(len(nonzero_heights)):
    find_surrounding_empty(board, nonzero_heights[x], nonzero_widths[x])
"""


show_board(board)
user_input(board)
show_board(board)
find_nonzero(board)
