# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:08:34 2023

@author: Nate
"""

def run_game(px,po):
    
    #clear board - -1 is X, +1 is 0
    board = [[0,0,0],[0,0,0],[0,0,0]]
    
    #0 is game in prog, -1 is X wins, +1 is O wins, any other number is draw
    game_state = 0
    
    #X starts
    next_player = -1 

    while game_state == 0 :
        mx = 0
        my = 0
        if next_player == -1:
            mx,my = px.move(board)
        else:
            mx,my = po.move(board)
            
        #make sure space isn't taken
        if board[mx][my] == 0:
            board[mx][my] = next_player
        
        #check for victory
        #rows and cols
        for i in range(3):
            if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                game_state = next_player
            if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                game_state = next_player
        #check diagonals
            if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
                game_state = next_player
            if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
                game_state = next_player
        
        #check if board is full
        board_full = True
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board_full = False
        
        if board_full == True:
            game_state = 2
        next_player *= -1
    
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
    

class pc_player:
    
    _mark = 0
    
    def __init__(marker):
        self._mark = marker
    
    def move(board):
        print("Player " + str(self._mark) + "'s turn to move")
        print ("\n")
        
        
        
