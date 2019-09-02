import numpy

#Variables
PLAYERS= 2
boardW = 5
boardH = 5
board = numpy.zeros((boardW,boardH))
step = 0
winLength = 3

#Functions
def drawBoard():
    global step
    print("\n Step:", step, "\n")
    for i in range(0,len(board)):
        for j in numpy.flipud(board)[i]:
            print('{:>4}'.format(getSym(j)), end = "")
        print("\n")
    step+=1;

symbols="■XOABCDEFGHIJKLMNOPQRSTUVWXZ"

def getSym(n):
    return symbols[int(n)]

def move(player):
    while(True):
        row, column = eval(input("Player "+str(player)+" Move, Enter coordinates: "))
        try:
            if board[column-1][row-1]==0:
                board[column-1][row-1]=player
                break;
            else:
                print("You can't move there! Choose a blank spot!")
        except:
            print("Coordinates Out of Bounds, Try again!")

def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return i, i+len(small)
    return False

def getState():
    #checks columns
    for r in range(board.shape[0]):
        for p in range(1, PLAYERS+1):
            #if all(board[w,:] == numpy.full((board.shape[1]),p)):
            if contains(numpy.full(3,p), board[r,:]):
                return p
    #checks rows
    for c in range(board.shape[1]):
        for p in range(1, PLAYERS+1):
            #if all(board[:,h] == numpy.full((board.shape[0]),p)):
            if contains(numpy.full(winLength,p), board[:,c]):
                return p
    #check diagonals
    maxDiagonalOffset=max(board.shape[0], board.shape[1])-(winLength-1)
    for o in range(-maxDiagonalOffset+1,maxDiagonalOffset):
        for p in range(1, PLAYERS+1):
            for i in [-1,1]:
                if contains(numpy.full(winLength,p), numpy.diagonal(board[::i],o)):
                    return p
    #check for no more blanks
    if 0 not in board:
        return "Tied"
    return 0
    
#Main loop
while(True):
    step = 0
    board = numpy.zeros((5,5))
    print(" ======= EXTREME TIC TAC TOE  ======= ")
    #Variables
    PLAYERS=int(input("How many players?: "))
    boardW = int(input("What's the board's width?: "))
    boardH = int(input("What's the board's height?: "))
    board = numpy.zeros((boardW,boardH))
    step = 0
    winLength = int(input("How many in a row to win?: "))
    print(" ======= GAME STARTING...  ======= ")
    while(True):
        drawBoard()
        if getState()=="Tied":
            print("The game tied!")
            break;
        elif getState()>0:
            print("Player", getState(), "Won!")
            break;
        
        move((step-1)%PLAYERS+1)
    if input("Keep playing?(press y): ").lower() != 'y':
        break
    


