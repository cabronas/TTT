from BoardInteractions import *
from random import *


# Main AI Turn logic
def MakeAiTurn(Board, Side):
    # Check if Ai can win in 1 move
    AiBoard = Board
    for x in range(3):
        for y in range(3):
            AiBoard = Board
            # Check if move is legal
            if CheckIfLegal(AiBoard, x, y):
               AiBoard[x][y] = Side
               # See if move is a winning one
               if GameOver(AiBoard, Side) == Side:
                   return MakeTurn(Board, x, y, Side)
    # Default to random move
    return MakeAiRandomTurn(Board, Side)


# Generates random coordinates and makes a turn
def MakeAiRandomTurn(Board, Side):
    x, y = CreateRandomCoordinates()
    if CheckIfLegal(Board,x,y):
        return MakeTurn(Board, x, y, Side)
    else:
        return MakeAiRandomTurn(Board, Side)


# Create x and y for random turn
def CreateRandomCoordinates():
    x = randint(0,2)
    y = randint(0,2)
    return x,y