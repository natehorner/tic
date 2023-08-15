# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:41:11 2023

@author: Nate
"""

import players
import tic

#px = players.pc_player(-1)
#po = players.consec_player(1)

#px = players.consec_player(-1)
px = players.learning_player(-1)
po = players.learning_player(1)


xwin = 0
owin = 0
tie = 0
games = 0

for i in range(10):
    score = tic.run_game(px,po)
    games += 1
    if score == -1:
        xwin += 1
    elif score == 1:
        owin += 1
    else :
        tie += 1

print("Score after " + str(games) + " games (X, O, Tie): " + str(xwin) + ", " 
      + str(owin) + ", " + str(tie))

for i in range(990):
    score = tic.run_game(px,po)
    games += 1
    if score == -1:
        xwin += 1
    elif score == 1:
        owin += 1
    else :
        tie += 1
    

print("Score after " + str(games) + " games (X, O, Tie): " + str(xwin) + ", " 
      + str(owin) + ", " + str(tie))


for i in range(9000):
    score = tic.run_game(px,po)
    games += 1
    if score == -1:
        xwin += 1
    elif score == 1:
        owin += 1
    else :
        tie += 1
    if i%1000 == 0 and i != 0:
        print("Finished iteration " + str(i))

print("Score after " + str(games) + " games (X, O, Tie): " + str(xwin) + ", " 
      + str(owin) + ", " + str(tie))

