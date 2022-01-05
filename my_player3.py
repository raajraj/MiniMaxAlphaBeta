import os
import copy
import time
import random
import numpy as np

N = 5
alpha = float('-inf')
beta = float('inf')

def notSuicide(board, i, j):
    notSuicide = 1
    if((i > 0) & (i < 4) & (j > 0) & (j < 4)):
        if((board[i][j-1] == opposer) & (board[i][j+1] == opposer) & (board[i+1][j] == opposer) & (board[i-1][j] == opposer)):
            notSuicide = 0
    elif(i == 0):
        if(j == 0):
            if((board[i][j+1] == opposer) & (board[i+1][j] == opposer)):
                notSuicide = 0
        elif(j == 4):
            if((board[i][j-1] == opposer) & (board[i+1][j] == opposer)):
                notSuicide = 0
        else:
            if((board[i][j-1] == opposer) & (board[i+1][j] == opposer) & (board[i][j+1] == opposer)):
                notSuicide = 0
    elif(i == 4):
        if(j == 4):
            if((board[i][j-1] == opposer) & (board[i-1][j] == opposer)):
                notSuicide = 0
        elif(j == 0):
            if((board[i][j+1] == opposer) & (board[i-1][j] == opposer)):
                notSuicide = 0
        else:
            if((board[i][j-1] == opposer) & (board[i-1][j] == opposer) & (board[i][j+1] == opposer)):
                notSuicide = 0
    else:
        if(j == 0):
            if((board[i][j+1] == opposer) & (board[i-1][j] == opposer) & (board[i+1][j] == opposer)):
                notSuicide = 0
        else:
            if((board[i][j-1] == opposer) & (board[i-1][j] == opposer) & (board[i+1][j] == opposer)):
                notSuicide = 0
    return notSuicide

def suicide(board, i, j, forPlayer):
    suicide = 0
    if(forPlayer):
        if((i > 0) & (i < 4) & (j > 0) & (j < 4)):
            if((board[i][j-1] == opposer) & (board[i][j+1] == opposer) & (board[i+1][j] == opposer) & (board[i-1][j] == opposer)):
                suicide = 1
        elif(i == 0):
            if(j == 0):
                if((board[i][j+1] == opposer) & (board[i+1][j] == opposer)):
                    suicide = 1
            elif(j == 4):
                if((board[i][j-1] == opposer) & (board[i+1][j] == opposer)):
                    suicide = 1
            else:
                if((board[i][j-1] == opposer) & (board[i+1][j] == opposer) & (board[i][j+1] == opposer)):
                    suicide = 1
        elif(i == 4):
            if(j == 4):
                if((board[i][j-1] == opposer) & (board[i-1][j] == opposer)):
                    suicide = 1
            elif(j == 0):
                if((board[i][j+1] == opposer) & (board[i-1][j] == opposer)):
                    suicide = 1
            else:
                if((board[i][j-1] == opposer) & (board[i-1][j] == opposer) & (board[i][j+1] == opposer)):
                    suicide = 1
        else:
            if(j == 0):
                if((board[i][j+1] == opposer) & (board[i-1][j] == opposer) & (board[i+1][j] == opposer)):
                    suicide = 1
            else:
                if((board[i][j-1] == opposer) & (board[i-1][j] == opposer) & (board[i+1][j] == opposer)):
                    suicide = 1
    else:
        if((i > 0) & (i < 4) & (j > 0) & (j < 4)):
            if((board[i][j-1] == player) & (board[i][j+1] == player) & (board[i+1][j] == player) & (board[i-1][j] == player)):
                suicide = 1
        elif(i == 0):
            if(j == 0):
                if((board[i][j+1] == player) & (board[i+1][j] == player)):
                    suicide = 1
            elif(j == 4):
                if((board[i][j-1] == player) & (board[i+1][j] == player)):
                    suicide = 1
            else:
                if((board[i][j-1] == player) & (board[i+1][j] == player) & (board[i][j+1] == player)):
                    suicide = 1
        elif(i == 4):
            if(j == 4):
                if((board[i][j-1] == player) & (board[i-1][j] == player)):
                    suicide = 1
            elif(j == 0):
                if((board[i][j+1] == player) & (board[i-1][j] == player)):
                    suicide = 1
            else:
                if((board[i][j-1] == player) & (board[i-1][j] == player) & (board[i][j+1] == player)):
                    suicide = 1
        else:
            if(j == 0):
                if((board[i][j+1] == player) & (board[i-1][j] == player) & (board[i+1][j] == player)):
                    suicide = 1
            else:
                if((board[i][j-1] == player) & (board[i-1][j] == player) & (board[i+1][j] == player)):
                    suicide = 1
    return suicide

def checkScore(board):
    points = 0
    for i in range(N):
        for j in range(N):
            if(board[i][j] == opposer):
                if(suicide(board, i, j, 0)):
                    points = points + 100
                if(((i == 1) & (j == 1)) | ((i == 2) & (j == 2)) | ((i == 2) & (j == 1)) | ((i == 1) & (j == 2))):
                    if((board[i][j] == board[i][j+1]) & (board[i][j] == board[i+1][j])):
                        if((board[i][j-1] == player) & (board[i+1][j-1] == player) & (board[i-1][j] == player) & (board[i-1][j+1] == player)):
                            points = points + 20
                            if((board[i+2][j] == player) & (board[i+1][j+1] == player) & (board[i][j+2] == player)):
                                points = points + 100
                elif(((i == 4) & (j == 1)) | ((i == 4) & (j == 2))):
                    if((board[i][j] == board[i][j+1]) & (board[i][j] == board[i-1][j])):
                        if((board[i][j-1] == player) & (board[i-1][j-1] == player) & (board[i-1][j+1] == player) & (board[i][j+2] == player)):
                            points = points + 20
                            if((board[i-2][j] == player):
                                points = points + 100
                elif((i == 4) & (j == 3)):
                    if((board[i][j] == board[i][j+1]) & (board[i][j] == board[i-1][j])):
                        if((board[3][4] == player) & (board[2][3] == player) & (board[3][2] == player) & (board[4][2] == player)):
                            points = points + 120
                    elif((board[i][j] == board[i][j-1]) & (board[i][j] == board[i-1][j])):
                        if((board[4][1] == player) & (board[3][2] == player) & (board[2][3] == player) & (board[3][4] == player) & (board[4][4] == player)):
                            points = points + 120
                elif((board[0][0] == opposer) & (board[0][1] == opposer) & (board[1][0] == opposer)):
                    if((board[2][0] == player) & (board[1][1] == player) & (board[0][2] == player)):
                        points = points + 120
                elif((board[4][4] == opposer) & (board[4][3] == opposer) & (board[3][4] == opposer)):
                    if((board[4][2] == player) & (board[3][3] == player) & (board[2][4] == player)):
                        points = points + 120
                elif((board[0][4] == opposer) & (board[0][3] == opposer) & (board[1][4] == opposer)):
                    if((board[0][2] == player) & (board[1][3] == player) & (board[2][4] == player)):
                        points = points + 120
                elif((board[4][0] == opposer) & (board[3][0] == opposer) & (board[4][1] == opposer)):
                    if((board[2][0] == player) & (board[3][1] == player) & (board[4][2] == player)):
                        points = points + 120
                if(((i == 1) & (j == 2)) | ((i == 1) & (j == 3)) | ((i == 2) & (j == 2)) | ((i == 2) & (j == 3))):
                    if((board[i][j] == board[i][j-1]) & (board[i][j] == board[i+1][j])):
                        if((board[i][j-2] == player) & (board[i+1][j-1] == player) & (board[i-1][j] == player) & (board[i-1][j-1] == player)):
                            points = points + 20
                            if((board[i+2][j] == player) & (board[i+1][j+1] == player) & (board[i][j+1] == player)):
                                points = points + 100
                if((j == 1) & (i != 0) & (i != 4)):
                    if((board[i][j] == board[i][j+1]) & (board[i][j] == board[i][j+2])):
                        if((board[i-1][j] == player) & (board[i-1][j+1] == player) & (board[i-1][j+2] == player)):
                            points = points + 30
                            if((board[i+1][j] == player) & (board[i+1][j+1] == player) & (board[i+1][j+2] == player)):
                                points = points + 30
                                if((board[i][j-1] == player) & (board[i][j+3] == player)):
                                    points = points + 30
                elif((j == 0) & (i < 3)):
                    if((board[i][j] == board[i+1][j]) & (board[i][j] == board[i+2][j])):
                        if((board[i][j+1] == player) | (board[i+1][j+1] == player) | (board[i+2][j+2] == player)):
                            points = points + 45
                        if(i != 0):
                            if((board[i-1][j] == player) & (board[i][j] == player)):
                                points = points + 80
                elif((j == 4) & (i < 3)):
                    if((board[i][j] == board[i+1][j]) & (board[i][j] == board[i+2][j])):
                        if((board[i][j-1] == player) & (board[i+1][j-1] == player) & (board[i+2][j-2] == player)):
                            points = points + 45
                        if(i != 0):
                            if((board[i-1][j] == player) & (board[i][j] == player)):
                                points = points + 80
                if(i < N-1):
                    if(board[i][j] == board[i+1][j]):
                        if(j < N-1):
                            if((board[i][j+1] == player) & (board[i+1][j+1] == player)):
                                points = points + 15
                                if(j == 0):
                                    if(i == 3):
                                        if(board[i-1][j] == player):
                                            points = points + 100
                                    elif(i == 0):
                                        if(board[i+2][j] == player):
                                            points = points + 100
                                    else:
                                        if((board[i-1][j] == player) & (board[i+2][j] == player)):
                                            points = points + 100
                                elif((board[i][j-1] == player) & (board[i+1][j-1] == player)):
                                    points = points + 15
                                    if(i == 0):
                                        if(board[i+2][j] == player):
                                            points = points + 100
                                    elif(i == 3):
                                        if(board[i-1][j] == player):
                                            points = points + 100
                                    else:
                                        if((board[i-1][j] == player) & (board[i+2][j] == player)):
                                            points = points + 100
                        else:
                            if((board[i][j-1] == player) & (board[i+1][j-1] == player)):
                                    points = points + 15
                                    if(i == 0):
                                        if(board[i+2][j] == player):
                                            points = points + 100
                                    elif(i == 3):
                                        if(board[i-1][j] == player):
                                            points = points + 100
                                    else:
                                        if((board[i-1][j] == player) & (board[i+2][j] == player)):
                                            points = points + 100
                if(j < N-1):
                    if(board[i][j] == board[i][j+1]):
                        if(i < N-1):
                            if((board[i+1][j] == player) & (board[i+1][j+1] == player)):
                                points = points + 10
                                if(i > 0):
                                    if((board[i-1][j] == player) & (board[i-1][j+1] == player)):
                                        points = points + 10
                                        if(j == 0):
                                            if(board[i][j+2] == player):
                                                points = points + 100
                                        elif(j == 3):
                                            if(board[i][j-1] == player):
                                                points = points + 100
                                        else:
                                            if((board[i][j-1] == player) & (board[i][j+2] == player)):
                                                points = points + 100
                                    else:
                                        if(board[i][j-1] == player):
                                            points = points + 100
                                else:
                                    points = points + 60
                        else:
                            if((board[i-1][j] == player) & (board[i-1][j+1] == player)):
                                points = points + 10
                                if(j == 0):
                                    if(board[i][j+2] == player):
                                        points = points + 60
                                elif(j == 3):
                                    if(board[i][j-1] == player):
                                        points = points + 60
                                else:
                                    if((board[i][j+2] == player) & (board[i][j-1] == player)):
                                        points = points + 60
            if(board[i][j] == player):
                if(suicide(board, i, j, 1)):
                    points = points - 50
                if((i != 0) & (i != 4) & (j != 0) & (j != 4)):
                    points = points + 2
                    if((board[i-1][j] == opposer) | (board[i+1][j] == opposer) | (board[i][j+1] == opposer) | (board[i][j-1] == opposer)):
                        points = points + 10
                    if((board[i-1][j-1] == opposer) | (board[i+1][j+1] == opposer) | (board[i+1][j-1] == opposer) | (board[i-1][j+1] == opposer)):
                        points = points + 10
                    #if((board[i-1][j] == player) | (board[i+1][j] == player) | (board[i][j+1] == player) | (board[i][j-1] == player)):
                        #points = points + 4
                    #if((board[i-1][j-1] == player) | (board[i+1][j+1] == player) | (board[i+1][j-1] == player) | (board[i-1][j+1] == player)):
                       # points = points + 4
                elif(i == 0):
                    if(j == 0):
                        if((board[i][j+1] == opposer) | (board[i+1][j] == opposer)):
                            points = points + 3
                        if(board[1][1] == player):
                            points = points + 3
                    elif(j == 4):
                        if((board[i][j-1] == opposer) | (board[i+1][j] == opposer)):
                            points = points + 3
                        if(board[3][1] == player):
                            points = points + 3
                    else:
                        if((board[i][j-1] == opposer) | (board[i+1][j] == opposer) | (board[i][j+1] == opposer)):
                            points = points + 6
                        if((board[i+1][j+1] == opposer) | (board[i+1][j-1] == opposer)):
                            points = points + 2
                elif(i == 4):
                    if(j == 4):
                        if((board[i][j-1] == opposer) | (board[i-1][j] == opposer)):
                            points = points + 3
                        if(board[3][3] == opposer):
                            points = points + 3
                    elif(j == 0):
                        if((board[i][j+1] == opposer) | (board[i-1][j] == opposer)):
                            points = points + 3
                        if(board[3][1] == opposer):
                            points = points + 3
                    else:
                        if((board[i][j-1] == opposer) | (board[i-1][j] == opposer) | (board[i][j+1] == opposer)):
                            points = points + 4
                        if((board[i-1][j-1] == opposer) | (board[i-1][j+1] == opposer)):
                            points = points + 10
                else:
                    if(j == 0):
                        if((board[i][j+1] == opposer) | (board[i-1][j] == opposer) | (board[i+1][j] == opposer)):
                            points = points + 4
                        if((board[i+1][j+1] == opposer) | (board[i][j+1] == opposer)):
                            points = points + 10
                    else:
                        if((board[i][j-1] == opposer) | (board[i-1][j] == opposer) | (board[i+1][j] == opposer)):
                            points = points + 4
                        if((board[i-1][j-1] == opposer) | (board[i+1][j-1] == opposer)):
                            points = points + 10
    return points

# minimax algorithm
def minimax(board, depth, isMaximizing, alpha, beta):
    if(depth == 3):
        return checkScore(board)
    if(isMaximizing):
        bestScore = float('-inf')
        for i in range(N):
            for j in range(N):
                if((board[i][j] == 0) & (notSuicide(currentBoard, i, j))):
                    board[i][j] = player
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = 0
                    bestScore = max(bestScore, score)
                    alpha = max(alpha, score)
                    if(beta <= alpha):
                        break
        return bestScore
    else:
        minScore = float('inf')
        for i in range(N):
            for j in range(N):
                if((board[i][j] == 0) & (notSuicide(currentBoard, i, j))):
                    board[i][j] = opposer
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = 0
                    minScore = min(minScore, score)
                    beta = min(beta, score)
                    if(beta <= alpha):
                        break
        return minScore

# calls minimax algorithm
def nextBestMove(player, previousBoard, currentBoard):
    if(np.all(currentBoard == 0)):
        return (2,2)
    score = 0
    bestScore = float('-inf')
    bestMove = (-1, -1)
    zeroes = np.count_nonzero(currentBoard == 0)
    if(zeroes <= 1):
        return bestMove
    else:
        for i in range(N):
            for j in range(N):
                if((currentBoard[i][j] == 0) & (previousBoard[i][j] == 0) & (notSuicide(currentBoard, i, j))):
                    currentBoard[i][j] = player
                    score = minimax(currentBoard, 0, False, alpha, beta)
                    currentBoard[i][j] = 0
                    if(score > bestScore):
                        bestScore = score
                        bestMove = (i,j)
    return bestMove

def writePass():
    f = open('output.txt', 'w')
    f.write("PASS")
    return

# open the file
f = open("input.txt", "r")
player = int(f.readline())
opposer = 0
if(player == 1):
    opposer = 2
else:
    opposer = 1

# store previous board
with open("input.txt") as myfile:
    previousBoard = np.zeros((5,5))
    for x in range(5):
        j = 0
        for y in f.readline():
            if(y != '\n'):
                y = int(y)
                previousBoard[x][j] = y
                j = j + 1

# store current board
with open("input.txt") as myfile:
    currentBoard = np.zeros((N,N))
    for x in range(N):
        j = 0
        for y in f.readline():
            if(y != '\n'):
                y = int(y)
                currentBoard[x][j] = y
                j = j + 1

# get the move
move = nextBestMove(player, previousBoard, currentBoard)

# output move
f = open('output.txt', 'w')
if(move == (-1,-1)):
    writePass()
else:
    f.write(str(move[0]) + ',' + str(move[1]))
    
