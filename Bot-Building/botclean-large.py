# MegaMaid is a robot whose function is to move through a matrix and clean 
# all of its dirty cells. It's positioned in some cell of an  matrix of dirty 
# (d) and clean (-) cells. It can perform five types of operations:
# LEFT: Move one cell to the left.
# RIGHT: Move one cell to the right.
# UP: Move one cell up.
# DOWN: Move one cell down.
# CLEAN: Clean the cell.
# Given the robot's current location and the configuration of dirty and clean cells 
# in the matrix, print the next operation MegaMaid will perform 
# (e.g., UP, CLEAN, etc.) on a new line.

# Link: https://www.hackerrank.com/challenges/botcleanlarge
# Developer: Murillo Grubler

# import library
import math

# Update cost that bot need to arrive the dirty
def update_position(posr, posc, dirties):
    nearest_dirt = []
    for i in range(len(dirties)):
        # Euclidean distance
        result = math.sqrt(((dirties[i][0] - posr) ** 2) + ((dirties[i][1] - posc) ** 2))
        nearest_dirt.append(result)
    return [x for (y,x) in sorted(zip(nearest_dirt,dirties))]

# Set the bot in your new position
def next_move(posx, posy, dimx, dimy, board):
    dirties = []
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j] == 'd':
                dirties.append([i, j])

    next_dirt = update_position(posx, posy, dirties)
    if next_dirt[0][0] < posx:
        print('UP')
    elif next_dirt[0][0] > posx:
        print('DOWN')
    elif next_dirt[0][1] < posy:
        print('LEFT')
    elif next_dirt[0][1]  > posy:
        print('RIGHT')
    else:
        print('CLEAN')

# Set data
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
