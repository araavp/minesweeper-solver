# Minesweeper Solver
# For expert mode on minesweeperonline.com
# 16 x 30 board with 99 mines

import keyboard
import numpy as np


board_height = 16
board_width = 30
board = [[0 for x in range(board_width)] for y in range(board_height)]
print(np.matrix(board))
total_mines = 99


def show_board(mine_board):
    print(mine_board)


def user_input():
    while True:
        try:
            height = int(input("Enter row number: ")) - 1
            width = int(input("Enter column number: ")) - 1
            number = int(input("What is the number at that location: "))
            board[height][width] = number
        except ValueError:
            user_quit = input("Press q to quit or c to continue")
            if user_quit == 'q':
                break
            elif user_quit == 'c':
                continue



user_input()
print(np.matrix(board))
print("reached here")



