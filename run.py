# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:41:11 2023

@author: Nate
"""

import players
import tic

#px = players.pc_player(-1)
#px = players.consec_player(-1)
#px = players.learning_player(-1)

#po = players.consec_player(1)
po = players.learning_player(1)


#first game
px = players.pc_player(-1)
tic.run_game(px,po)


#play 100,000 times
px = players.learning_player(-1)
for i in range(100):
    tic.run_n_games(px,po,1000)




#final game
px = players.pc_player(-1)
tic.run_game(px,po)
