# TTC
# 0=Empty, 1=X, 2=O
import os
from BoardInteractions import *
from PlayerActions import *
from AiActions import *

# Variables
RealBoard = []
RealBoard = DefBoard()
PlayerSide = 1
AiSide = 1

# Initiate game variables
def Start():
    Board = []
    PSide, ASide = 1 , 1
    Board = DefBoard()
    PSide = int(AskPlayerSide())
    if PSide == 1:
        ASide = 2
    return Board, PSide, ASide

#Starts the game
def Game(Board,PSide,ASide):
    CurrentTurn = 1
    GameEnd = 0
    while GameEnd == 0:
        #Each side takes turns
        if PSide == CurrentTurn:
            MakePlayerTurn(Board, PSide, False)
            GameEnd = GameOver(Board, PSide)
        else:
            MakeAiTurn(Board, AiSide)
            GameEnd = GameOver(Board, ASide)
        #Switch turns
        if CurrentTurn == 1: CurrentTurn = 2
        else: CurrentTurn = 1
    #End
    os.system('clear')
    OutPutBoard(Board)
    if GameEnd == 3:
        print("Draw")
    elif GameEnd == PSide:
        print("Player won")
    else:
        print("AI won")
    return
# MAIN
while True:
    RealBoard, PlayerSide, AiSide = Start()
    Game(RealBoard, PlayerSide, AiSide)
#Game