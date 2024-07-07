from board import Board
from agent import Agent
import random

class MinimaxAgent(Agent):
    def __init__(self, player, depth=3):
        self.player = player
        self.depth = depth

    def next_action(self, obs):
        best_action, _ = self.minimax(obs, self.player, self.depth, float('-inf'), float('inf'))
        return best_action

    def minimax(self, board: Board, player, depth, alpha, beta):
        end, winner = board.is_end(player)
        if end:
            return None, 1 if winner == self.player else -1
        if depth == 0:
            return None, self.heuristic_utility(board)

        if player == self.player:
            max_eval = float('-inf')
            best_action = None
            for action in board.get_possible_actions():
                new_board = board.clone()
                new_board.play(action)
                _, eval = self.minimax(new_board, (player % 2) + 1, depth - 1, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_action = action
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return best_action, max_eval
        else:
            min_eval = float('inf')
            best_action = None
            for action in board.get_possible_actions():
                new_board = board.clone()
                new_board.play(action)
                _, eval = self.minimax(new_board, (player % 2) + 1, depth - 1, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_action = action
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return best_action, min_eval

    def heuristic_utility(self, board: Board):
        # Heurística 1:cantidad de monedas restantes
        return -board.grid.sum()
        # Heurística 2: Heurística basada en la diferencia de monedas
        #player_coins = sum(sum(1 for cell in row if cell == self.player) for row in board.grid)
        #opponent_coins = sum(sum(1 for cell in row if cell == (self.player % 2) + 1) for row in board.grid)
        #return player_coins - opponent_coins

