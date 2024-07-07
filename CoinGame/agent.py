from abc import ABC, abstractmethod

import numpy as np
from board import Board

class Agent(ABC):

    @abstractmethod
    def __init__(self, player):
        self.player = player
        self.opponent = 2 if player == 1 else 1

    @abstractmethod
    def next_action(self, obs):
        _, action = self.minimax(obs, self.player, True, 0)
        return action
    
    def minimax(self, board, player, maximizing, depth):
        done, winner = board.is_end(player)
        if done:
            if winner == self.player:
                return 1, None
            elif winner == self.opponent:
                return -1, None
            else:
                return 0, None
        
        if maximizing:
            max_eval = float('-inf')
            best_action = None
            for action in board.get_possible_actions():
                new_board = board.clone()
                new_board.play(action)
                eval, _ = self.minimax(new_board, self.opponent, False, depth + 1)
                if eval > max_eval:
                    max_eval = eval
                    best_action = action
            return max_eval, best_action
        else:
            min_eval = float('inf')
            best_action = None
            for action in board.get_possible_actions():
                new_board = board.clone()
                new_board.play(action)
                eval, _ = self.minimax(new_board, self.player, True, depth + 1)
                if eval < min_eval:
                    min_eval = eval
                    best_action = action
            return min_eval, best_action
    
    @abstractmethod
    def heuristic_utility(self, board: Board):
        # A simple heuristic utility function that returns the count of remaining coins
        return -np.sum(board.grid)