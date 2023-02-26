import os
from BoardInteractions import *


# Check if variable is int type and is digit
def CheckIfValidInt(x):
    try:
        if int(x):
            return True
        else:
            return False
    except:
        return False


# Ask player side. X=1, O=2
def AskPlayerSide():
    print("X=1, O=2")
    Side = input()
    if Side == "1" or Side == "2":
        return Side
    else:
        print("Incorrect input")
        return AskPlayerSide()


# Input valid x and y coordinates for board move
def InputPlayerCoordinates():
    print("Enter coordinates ")
    strx, stry = "0", "0"
    try:
        print("Incorrect input, try again")
        strx, stry = input().split()
    except:
        return InputPlayerCoordinates()
    # Check if input is int and a digit
    if CheckIfValidInt(strx) and CheckIfValidInt(stry):
        x = int(strx) - 1
        y = int(stry) - 1
        # Check if input is within board range
        if 0 <= x <= 2 and 0 <= y <= 2:
            return x, y
        else:
            print("Incorrect range, try again")
            return InputPlayerCoordinates()
    else:
        print("Incorrect input, try again")
        return InputPlayerCoordinates()


# Takes coordinates and makes player turn
def MakePlayerTurn(Board, Side, Illegal):
    Clear()
    if Illegal==True:
        print("Illegal move, try again")
    OutPutBoard(Board)
    x, y = InputPlayerCoordinates()
    if CheckIfLegal(Board, x, y):
        return MakeTurn(Board, x, y, Side)
    else:
        return MakePlayerTurn(Board, Side, True)
