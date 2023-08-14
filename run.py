# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:41:11 2023

@author: Nate
"""

import players
import tic

px = players.pc_player(-1)
po = players.consec_player(1)

tic.run_game(px,po)

