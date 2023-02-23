import os


# Clear Screen
def Clear():
    os.system('clear')


# Initialise board for play
def DefBoard():
    Board = []
    for i in range(3):
        Column = []
        for j in range(3):
            Column.append(0)
        Board.append(Column)
    return Board


# Output board to console
def OutPutBoard(Board):
    Character = ""
    for a in range(3):
        for b in range(3):
            if Board[a][b] == 0:
                Character = "[ ]"
            elif Board[a][b] == 1:
                Character = "[X]"
            elif Board[a][b] == 2:
                Character = "[O]"
            print(Character, " ", end='')
        print()


# Alter the board
def MakeTurn(Board, x, y, Side):
    Board[int(x)][int(y)] = Side
    return Board


# Check if move can be made. True - legal, False - illegal
def CheckIfLegal(Board,x,y):
    if Board[x][y]!=0: return False
    else: return True


# Checks if game is over
# 0 - game is still not over, 1 or 2 - side won, 3 - draw
def GameOver(Board,Side):
    # Check if won - rows
    for x in range(3):
        if (Board[x] == [Side,Side,Side]):
            return Side
    # Check if won - columns
    count=0
    for y in range(3):
        for x in range(3):
            if Board[x][y] == Side:
                count += 1
        if count == 3:
            return Side
        else:
            count = 0
    # Check if won - diagonal
    count = 0
    for x in range(3):
        for y in range(3):
            if x == y:
                if Board[x][y] == Side:
                    count += 1
    if count == 3:
        return Side
    # Check if won - reverse diagonal
    count = 0
    for x in range(3):
        for y in range(3):
            if x + y == 2:
                if Board[x][y] == Side:
                    count += 1
    if count == 3:
        return Side
    # Check if draw
    for x in range(3):
        for y in range(3):
            if Board[x][y] == 0:
                return 0
    return 3

