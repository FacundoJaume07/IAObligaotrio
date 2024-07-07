from board import Board
from agent import Agent
import random

class ExpectimaxAgent(Agent):
    def __init__(self, player, depth=3):
        self.player = player
        self.depth = depth

    def next_action(self, obs):
        best_action, _ = self.expectimax(obs, self.player, self.depth)
        return best_action

    def expectimax(self, board: Board, player, depth):
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
                _, eval = self.expectimax(new_board, (player % 2) + 1, depth - 1)
                if eval > max_eval:
                    max_eval = eval
                    best_action = action
            return best_action, max_eval
        else:
            expected_eval = 0
            actions = board.get_possible_actions()
            for action in actions:
                new_board = board.clone()
                new_board.play(action)
                _, eval = self.expectimax(new_board, (player % 2) + 1, depth - 1)
                expected_eval += eval
            return None, expected_eval / len(actions)


    def heuristic_utility(self, board: Board):
        # Heurística 1:cantidad de monedas restantes
        return -board.grid.sum()
        # Heurística 2: Heurística basada en la diferencia de monedas
        #player_coins = sum(sum(1 for cell in row if cell == self.player) for row in board.grid)
        #opponent_coins = sum(sum(1 for cell in row if cell == (self.player % 2) + 1) for row in board.grid)
        #return player_coins - opponent_coins
    
     

