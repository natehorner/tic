# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:08:34 2023

@author: Nate
"""
from math import(floor)

boardsize = 3

def run_game(px,po):
    print("Starting Game")
    #clear board - -1 is X, +1 is 0
    board = [[0,0,0],[0,0,0],[0,0,0]]
    
    #0 is game in prog, -1 is X wins, +1 is O wins, any other number is draw
    game_state = 0
    
    #X starts
    curr_player = -1 

    while game_state == 0 :
        mx = 0
        my = 0
        if curr_player == -1:
            idx = px.move(board)
        else:
            idx = po.move(board)
        mx,my = idx_to_xy(idx)
        
        #make sure space isn't taken
        if board[mx][my] == 0:
            board[mx][my] = curr_player
        
        #check for victory
        sumdiag1 = 0
        sumdiag2 = 0
        #rows and cols
        for i in range(boardsize):
            sumrow = 0
            sumcol = 0
            
            for j in range(boardsize):
                sumrow += board[i][j]
                sumcol += board[j][i]
            if (abs(sumrow) == boardsize) or (abs(sumcol)==boardsize):
                game_state = curr_player
            sumdiag1 += board[i][i]
            sumdiag2 += board[i][boardsize-i-1]
        
        if (abs(sumdiag1) == boardsize) or (abs(sumdiag2) == boardsize):
            game_state = curr_player
                          
        #check if board is full
        board_full = True
        for i in range(boardsize):
            for j in range(boardsize):
                if board[i][j] == 0:
                    board_full = False
        
        if (board_full == True) and (game_state == 0):
            game_state = 2
        
        #switch active player
        curr_player *= -1
    
    #game is over
    if game_state == -1:
        px.winner(board)
        po.loser(board)
    elif game_state == 1:
        po.winner(board)
        px.loser(board)
    else :
        px.tie(board)
        po.tie(board)
    
    return

def mark_to_char(mark):
    if mark == -1:
        return 'X'
    else:
        return 'O'

def idx_to_xy(idx):
    x = floor(idx/boardsize)
    y = idx%boardsize
    return (x,y)
    
def xy_to_idx(x,y):
    idx = x*boardsize + y
    return idx
    
def printboard(board):
    outstr = ""
    
    for i in range(boardsize):
        if i > 0 :
            outstr += "--------------\n"
        
        for j in range(boardsize):
            
            if j > 0:
                outstr += "|"
            outstr += " "
            if board[i][j] == -1:
                outstr += " X "
            elif board[i][j] == 0:
                outstr += " " + str(xy_to_idx(i,j)) + " "
            elif board[i][j] == 1:
                outstr += " O "
        outstr += "\n"
            
    print(outstr)
    return
            
def checkmove(board,idx):
    if (idx < 0) or (idx > boardsize*boardsize):
        print("invalid move (" + str(idx) + "), try again")
        return False
    
    mx,my = idx_to_xy(idx)
    
    if board[mx][my] == 0:
        return True
    else:
        print("invalid move (" + str(idx) + "), try again")
        return False
