# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:12:30 2023

@author: Nate
"""

from abc import ( ABC, abstractmethod )
from tic import (printboard,checkmove,xy_to_idx)

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
    

xmark = -1
omark = 1
    
#human player - takes input from command line
class pc_player(player):
    
    _mark = 0
    """    
    def __init__(self, marker):
        self._mark = marker
        return
    """        
    def move(self, board):
        print("Player " + str(self._mark) + "'s turn to move")
        printboard(board)
        isvalid = False
        while isvalid == False:    
            user_input = input("Enter an open box's index: ")
            idx = int(user_input)
            isvalid = checkmove(board,idx)
            
        return idx
    
    def winner(self, board):
        print("Player " + str(self._mark) + " has won the game!")
        return
    
    def loser(self, board):
        print("Player " + str(self._mark) + " has lost the game!")
        return

    def tie(self, board):
        print("The game has ended in a tie")
        return


#test player - always chooses first open spot
class consec_player(player):
    
     _mark = 0

     def move(self, board):
         print("Player " + str(self._mark) + "'s turn to move")
         idx = -1
         for i in range(len(board)):
             for j in range(len(board[0])):
                 if board[i][j] == 0:
                     idx = xy_to_idx(i,j)
         return idx
     
     def winner(self, board):
         print("Player " + str(self._mark) + " has won the game!")
         return
     
     def loser(self, board):
         print("Player " + str(self._mark) + " has lost the game!")
         return

     def tie(self, board):
         print("The game has ended in a tie")
         return
     
        