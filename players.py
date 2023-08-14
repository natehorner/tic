# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:12:30 2023

@author: Nate
"""

from abc import ( ABC, abstractmethod )
from tic import (printboard,checkmove,xy_to_idx,mark_to_char)

class player(ABC):

    _mark = 0
    
    def __init__(self, marker):
        self._mark = marker
        return
    
    @abstractmethod
    def move(self,board):
        pass
    
    @abstractmethod
    def winner(self,board):
        pass
    
    @abstractmethod
    def loser(self,board):
        pass
    
    @abstractmethod
    def tie(self,board):
        pass
    
#human player - takes input from command line
class pc_player(player):
    
    _mark = 0
    """    
    def __init__(self, marker):
        self._mark = marker
        return
    """        
    def move(self, board):
        print("Player " + mark_to_char(self._mark) + "'s turn to move")
        printboard(board)
        isvalid = False
        while isvalid == False:    
            user_input = input("Enter an open box's index: ")
            idx = int(user_input)
            isvalid = checkmove(board,idx)
            
        return idx
    
    def winner(self, board):
        print("Player " + mark_to_char(self._mark) + " has won the game!")
        printboard(board)
        
        return
    
    def loser(self, board):
        print("Player " + mark_to_char(self._mark) + " has lost the game!")
        printboard(board)
        
        return

    def tie(self, board):
        print("The game has ended in a tie")
        printboard(board)
        
        return


#test player - always chooses first open spot
class consec_player(player):
    
     _mark = 0

     def move(self, board):
         #print("Player " + mark_to_char(self._mark) + "'s turn to move")
         idx = -1
         for i in range(len(board)):
             if idx != -1 :
                 break
             for j in range(len(board[0])):
                 if board[i][j] == 0:
                     idx = xy_to_idx(i,j)
                     break
                
         return idx
     
     def winner(self, board):
         #print("Player " + mark_to_char(self._mark) + " has won the game!")
         return
     
     def loser(self, board):
         #print("Player " + mark_to_char(self._mark) + " has lost the game!")
         return

     def tie(self, board):
         #print("The game has ended in a tie")
         return


#learning player
class learning_player(player):
    _mark = 0
    states = []
    state_to_val = {}
    
    learn_rate = 0.2
    rand_rate = 0.2
    decay_rate = 0.95
    
    def board_to_hash(self,board):
        arr = []
        for i in range(len(board)):
            arr.extend(board[i])
        return str(arr)
    
    def __init__(self, marker):
        self._mark = marker
        self.states = []
        self.state_to_val = {}
        return
    
    def move(self, board):
        
        #check if it will experiment and act randomly
        
        return
        
    def winner(self, board):

        return
     
    def loser(self, board):

        return

    def tie(self, board):

        return
    

    