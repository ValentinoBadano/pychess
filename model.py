import chess
from evaluate import *

class Model():
    def __init__(self):
        pass

    def search(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return evaluate(board)

        legal_moves = list(board.legal_moves)

        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_moves:
                new_board = board.copy()
                new_board.push(move)
                eval_score = search(new_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                new_board = board.copy()
                new_board.push(move)
                eval_score = search(new_board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval

    def choose_best_move(self, board, depth):
        legal_moves = list(board.legal_moves)
        best_move = None
        best_eval = float('-inf')

        for move in legal_moves:
            new_board = board.copy()
            new_board.push(move)

            quiescent_eval = self.search_quiescent(new_board, depth-1, float('-inf'), float('inf'), False)
            
            if quiescent_eval > best_eval:
                best_eval = quiescent_eval
                best_move = move

        return best_move

    def search_quiescent(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return evaluate(board)

        legal_captures = [move for move in board.legal_moves if board.is_capture(move)]

        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_captures:
                new_board = board.copy()
                new_board.push(move)
                eval_score = self.search_quiescent(new_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_captures:
                new_board = board.copy()
                new_board.push(move)
                eval_score = self.search_quiescent(new_board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval