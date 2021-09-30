"""
Name: Jeff Wang
UPI: jwan557
Description: A command lines sokoban game created with Python where
             a player must use wasd to push crates into holes.
"""


class Sokoban:
    def __init__(self, board):
        self.__board = board
        self.__width = len(board[0])
        self.__height = len(board)
        self.__num_of_holes = self.find_number_of_holes()
        self.__game_history = []  # list containing codes for all actions
        self.__player_moves = []  # coords for swaps when player moves
        self.__crate_moves = []  # swaps when crate move or goes in hole

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
        # the player always moves whenever the user has a valid input
        return len(self.__player_moves)

    def restart(self):
        while self.__game_history:
            self.undo()

    def undo(self):
        if self.__game_history:
            self.__game_history.pop()
            swap_coords1, swap_coords2 = self.__player_moves.pop()
            self.swap_squares(swap_coords1, swap_coords2)
            if self.__game_history:
                if self.__game_history[-1] == "crate_move":
                    swap_coords1, swap_coords2 = self.__crate_moves.pop()
                    self.swap_squares(swap_coords1, swap_coords2)
                    self.__game_history.pop()
                elif self.__game_history[-1] == "crate_in_hole":
                    crate_coords, hole_coords = self.__crate_moves.pop()
                    self.__board[crate_coords[0]][crate_coords[1]] = "#"
                    self.__board[hole_coords[0]][hole_coords[1]] = "o"
                    self.__num_of_holes += 1
                    self.__game_history.pop()

    def move(self, direction):
        player_coords = self.find_player()
        player_move_pos = self.get_move_location(
            direction, player_coords)

        if self.__board[player_move_pos[0]][player_move_pos[1]] == " ":
            self.move_player(player_coords, player_move_pos)

        elif self.__board[player_move_pos[0]][player_move_pos[1]] == "#":
            self.move_crate(direction, player_coords, player_move_pos)

    def get_move_location(self, direction, initial_coords):
        initial_row, initial_col = initial_coords
        # modulus allows player and crate to appear on other side of board
        if direction == "w":
            return (initial_row - 1) % self.__height, initial_col
        elif direction == "a":
            return initial_row, (initial_col - 1) % self.__width
        elif direction == "s":
            return (initial_row + 1) % self.__height, initial_col
        else:
            return initial_row, (initial_col + 1) % self.__width

    def move_player(self, player_coords, floor_coords):
        self.swap_squares(player_coords, floor_coords)
        swap_tuple = (player_coords, floor_coords)
        self.__game_history.append("player_move")
        self.__player_moves.append(swap_tuple)

    def move_crate(self, direction, player_coords, crate_coords):
        crate_move_coords = self.get_move_location(direction, crate_coords)
        crate_move_row, crate_move_col = crate_move_coords
        if self.__board[crate_move_row][crate_move_col] not in (" ", "o"):
            return
        elif self.__board[crate_move_row][crate_move_col] == " ":
            self.swap_squares(crate_coords, crate_move_coords)
            swap_tuple = (crate_coords, crate_move_coords)
            self.__game_history.append("crate_move")
            self.__crate_moves.append(swap_tuple)
        else:
            self.__board[crate_move_row][crate_move_col] = " "
            self.__board[crate_coords[0]][crate_coords[1]] = " "
            crate_hole_tuple = (crate_coords, crate_move_coords)
            self.__game_history.append("crate_in_hole")
            self.__crate_moves.append(crate_hole_tuple)
            self.__num_of_holes -= 1
        self.move_player(player_coords, crate_coords)

    def swap_squares(self, coord1, coord2):
        row1, col1 = coord1
        row2, col2 = coord2
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
