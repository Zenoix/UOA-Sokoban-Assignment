"""
Name: Jeff Wang
UPI: jwan557
Description: A command lines sokoban game created with Python where
             a player must use wasd to push crates into holes.
"""


class Sokoban:
    def __init__(self, board):
        self.__original_board = list(board)
        self.__board = board
        self.__width = len(board[0])
        self.__height = len(board)
        self.__num_of_holes = self.find_number_of_holes()
        self.__move_history = []

    def find_number_of_holes(self):
        number_of_holes = 0
        for row in range(len(self.__board)):
            for col in range(len(self.__board[0])):
                if self.__board[row][col] == "o":
                    number_of_holes += 1
        return number_of_holes

    def find_player(self):
        for row in range(len(self.__board)):
            for col in range(len(self.__board[0])):
                if self.__board[row][col] == "P":
                    return row, col

    def complete(self):
        return self.__num_of_holes == 0

    def get_steps(self):
        return len(self.__move_history) - 1

    def restart(self):
        # TODO Check that this works and the original board is not changed
        self.__board = self.__original_board

    def undo(self):
        if len(self.__move_history) != 0:
            swapped_square1, swapped_square2 = self.__move_history.pop()
            swap_row1, swap_col1 = swapped_square1
            swap_row2, swap_col2 = swapped_square2
            self.swap_squares(swap_row1, swap_col1, swap_row2, swap_col2)

    def move(self, direction):
        p_row, p_col = self.find_player()
        move_row, move_col = self.get_intended_square(direction, p_row, p_col)
        if self.__board[move_row][move_col] not in (" ", "#"):
            return
        elif self.__board[move_row][move_col] == " ":
            self.swap_squares(p_row, p_col, move_row, move_col)
            self.__move_history.append(((p_row, p_col), (move_row, move_col)))
        else:
            pass

    def get_intended_square(self, direction, player_row, player_col):
        if direction == "w":
            return (player_row - 1) % self.__height, player_col
        elif direction == "a":
            return player_row, (player_col - 1) % self.__width
        elif direction == "s":
            return (player_row + 1) % self.__height, player_col
        else:
            return player_row, (player_col + 1) % self.__width

    def swap_squares(self, row1, col1, row2, col2):
        temp = self.__board[row1][col1]
        self.__board[row1][col1] = self.__board[row2][col2]
        self.__board[row2][col2] = temp

    def __str__(self):
        # TODO Check if str output is correct
        output = ""
        for row in self.__board:
            output += " ".join(row) + "\n"
        # return the output with the last "\n" character
        return output[:-1]


def main(board):
    game = Sokoban(board)
    message = 'Press w/a/s/d to move, r to restart, or u to undo'
    print(message)
    while not game.complete():
        print(game)
        move = input('Move: ').lower()
        while move not in ('w', 'a', 's', 'd', 'r', 'u'):
            print('Invalid move.', message)
            move = input('Move: ').lower()
        if move == 'r':
            game.restart()
        elif move == 'u':
            game.undo()
        else:
            game.move(move)
    print(game)
    print(f'Game won in {game.get_steps()} steps!')


# This is here for you to test your code. You will need to test your code
# yourself for this assignment. Remove any testing code (including the code
# provided below) when you submit this file.
#
# The only code in your submission should be:
#   - the Sokoban class
#   - the main function
#
# There should be no other code included in your submission.
test_board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
main(test_board)
'''
test_board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', 'P', ' ', '#', ' ', ' ', ' ', '*'],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
a = Sokoban(test_board)
'''
