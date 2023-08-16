# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:12:30 2023

@author: Nate
"""
import random
from abc import ( ABC, abstractmethod )
from tic import (printboard,checkmove,xy_to_idx,mark_to_char,idx_to_xy)

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
#Can't switch from X to O! Won't understand!
class learning_player(player):
    _mark = 0
    states = []
    state_to_val = {}
    
    learn_rate = 0.2
    rand_rate = 0.05
    decay_rate = 0.9
    
    def board_to_hash(self,board):
        arr = []
        for i in range(len(board)):
            arr.extend(board[i])
        return str(arr)
    
    def board_copy(self,board):
        outboard = []
        for i in range(len(board)):
            outarr = []
            for j in range(len(board[0])):
                outarr.append(board[i][j])
            outboard.append(outarr)
        return outboard
    
    def __init__(self, marker):
        self._mark = marker
        self.states = []
        self.state_to_val = {}
        return
    
    def move(self, board):
        
        idx = -1
        use_random = False
        next_move_hash = 0
        
        #check if it will experiment and act randomly
        if random.random() <= self.rand_rate :
            use_random = True    
                
        else:
            val_max = 0
            
            #for each possible next move...
            for i in range(len(board)):
                for j in range(len(board[0])):
                    
                    #if the space is open...
                    if board[i][j] == 0 :        
                        #search for each in memory for best next move
                        next_board = self.board_copy(board)
                        next_board[i][j] = self._mark
                        next_board_hash = self.board_to_hash(next_board)
                        
                        next_move_val = self.state_to_val.get(next_board_hash)
                        if next_move_val != None:
                            if next_move_val > val_max:
                                val_max = next_move_val
                                next_move_hash = next_board_hash
                                idx = xy_to_idx(i,j)
            
            #if none found >0 use random number
            if val_max == 0:
                use_random = True
            else:
                #print("Found move value " + str(val_max) + " idx " + str(idx))
                pass
            
        #if random output
        if use_random == True:
            #find all possible moves
            moves = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        moves.append(xy_to_idx(i,j))
                    else:
                        #print("Space taken")
                        pass
            num_moves = len(moves)-1
            #print("number of moves " + str(num_moves+1))
            idx = moves[random.randint(0,num_moves)]
            next_board = self.board_copy(board)
            i,j = idx_to_xy(idx)
            next_board[i][j] = self._mark
            next_move_hash = self.board_to_hash(next_board)
            #print("Random experiment idx = " + str(idx))
        
        #insert next move on the state list and return
        self.states.append(next_move_hash)
        return idx
    
    def remember_game(self,reward):
        for state in reversed(self.states):
            prev_val = 0
            if self.state_to_val.get(state) == None:
                self.state_to_val[state] = 0
            else:
                prev_val = self.state_to_val.get(state)
            
            self.state_to_val[state] = prev_val + self.learn_rate*(reward*self.decay_rate - prev_val)
            #print("Hsh " + state + "prev val = " + str(prev_val) + " new val = " + str(self.state_to_val[state]))
        self.states.clear()
        return
    
    def winner(self, board):
        self.remember_game(1)
        return
     
    def loser(self, board):
        self.remember_game(0)
        return

    def tie(self, board):
        self.remember_game(0.1)
        return
    

    