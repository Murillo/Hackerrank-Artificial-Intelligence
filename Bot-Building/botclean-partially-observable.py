# The game Bot Clean took place in a fully observable environment, 
# i.e., the state of every cell was visible to the bot at all times. 
# Let us consider a variation of it where the environment is partially 
# observable. The bot has the same actuators and sensors. But the 
# sensors visibility is confined to its 8 adjacent cells.

# Link: https://www.hackerrank.com/challenges/botcleanv2
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

# It only obtains the visible field and set a new position 
# for the bot in relation to this visible field
def visible_field(board):
    bot_x = bot_y = 0
    visible = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            if board[i][j] != 'b':
                bot_x = board[i]
                bot_y = board[j]
            elif board[i][j] != 'o':
                row.append(board[i][j])
        if len(row) > 0:
            visible.append(row)
    return bot_x, bot_y, visible

# Set next action the bot
def next_move(posx, posy, board):
    posx, posy, board = visible_field(board)
    dirties = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                dirties.append([i, j])

    next_dirt = update_position(posx, posy, dirties)
    if (len(next_dirt) > 0):
        if next_dirt[0][1] < posy:
            print('LEFT')
        elif next_dirt[0][1]  > posy:
            print('RIGHT')
        elif next_dirt[0][0] < posx:
            print('UP')
        elif next_dirt[0][0] > posx:
            print('DOWN')
        else:
            print('CLEAN')
    else:
        print('LEFT')

# Set data
if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)
