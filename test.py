# This is here for you to test your code. You will need to test your code
# yourself for this assignment. Remove any testing code (including the code
# provided below) when you submit this file.
#
# The only code in your submission should be:
#   - the Sokoban class
#   - the main function
#
# There should be no other code included in your submission.

from assignment import Sokoban
from assignment import main

test_board = [
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
    [' ', 'P', ' ', '#', ' ', ' ', ' ', ' '],
    ['*', '*', '*', '*', '*', ' ', '#', '*'],
    ['*', 'o', ' ', ' ', ' ', ' ', ' ', '*'],
    ['*', ' ', ' ', ' ', ' ', ' ', 'o', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']
]
main(test_board)
