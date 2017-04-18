# Maze Escape is a popular 1 player game where a bot is trapped in a 
# maze and is expected to find its way out. In this version of the 
# game, 2 bots whose positions are not visible to each other are placed 
# at random points in the maze. the first bot to find its way out of 
# the maze wins the game.

# Link: https://www.hackerrank.com/challenges/maze-escape
# Developer: Murillo Grubler

# import library
import os
import math

# Set next action the bot
def next_move(player, board):
    print("Player: {}".format(player))
    move = ''
    # Start
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 and j == 1 and board[i][j] == '-':
                move = 'UP'
            if i == 0 and j == 1 and board[i][j] == '#':
                move = 'RIGHT'
    
    print(move)

# Start application
if __name__ == "__main__":
    # Set data
    player = int(input())
    board = [[j for j in input().strip()] for i in range(3)]  
    next_move(player, board)