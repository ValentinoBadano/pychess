from evaluate import evaluate

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_ai_move(self):
        board = self.view.board
        print("Calculating move...")
        move = self.model.choose_best_move(board, 4)
        print("Best move:", move)
        print("Current eval:", evaluate(board))
        return move