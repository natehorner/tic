# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:08:34 2023

@author: Nate
"""
from math import(floor)

boardsize = 3

def run_game(px,po):
    
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
        #rows and cols
        for i in range(boardsize):
            if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                game_state = curr_player
            if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                game_state = curr_player
        #check diagonals
            if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
                game_state = curr_player
            if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
                game_state = curr_player
        
        #check if board is full
        board_full = True
        for i in range(boardsize):
            for j in range(boardsize):
                if board[i][j] == 0:
                    board_full = False
        
        if board_full == True:
            game_state = 2
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
