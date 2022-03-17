#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:06:26 2022

@author: charlieroadhouse
"""

#Agent is inheriting from the data - this is the for the random agent

from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Tuple

from seoulai_gym.envs.checkers.base import Constants
from seoulai_gym.envs.checkers.rules import Rules
from seoulai_gym.envs.checkers.utils import generate_random_move
from seoulai_gym.envs.checkers.agents import Agent

class myAgent(Agent):
    def __init__(
            self,
            ptype: int,
    ):
        
        if ptype == Constants().DARK:
            name = "MyAgentDark"
        elif ptype == Constants().LIGHT:
            name = "MyAgentLight"
        else:
            raise ValueError
    
        super().__init__(name, ptype)
    
    def act(
        self,
        board: List[List],
    ) -> Tuple[int, int, int, int]:
        """
        Choose a piece and its possible moves randomly.
        Pieces and moves are chosen from all current valid possibilities.

        Args:
            board: information about positions of pieces.

        Returns:
            Current and new location of piece.
        """
        rand_from_row, rand_from_col, rand_to_row, rand_to_col = generate_random_move(
            board,
            self.ptype,
            len(board),
        )
        return rand_from_row, rand_from_col, rand_to_row, rand_to_col

    def consume(
        self,
        obs: List[List],
        reward: float,
        done: bool,
    ) -> None:
        """Agent processes information returned by environment based on agent's latest action.
        Random agent does not need `reward` or `done` variables, but this method is called anyway
        when used with other agents.

        Args:
            board: information about positions of pieces.
            reward: reward for perfomed step.
            done: information about end of game.
        """
        pass

class MyRandomAgentLight(myAgent):
    def __init__(
        self,
    ):
        super().__init__(Constants().LIGHT)