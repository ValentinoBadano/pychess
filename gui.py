import chess
import chess.svg
import chess.engine
import tkinter as tk
import sounds
from PIL import Image, ImageTk

class ChessGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ajedrez re piola")
        self.master.iconbitmap("img/chess.ico")
        self.master.resizable(False, False)

        self.board = chess.Board()

        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.image_references = []  

        self.update_board()

        self.canvas.bind("<Button-1>", self.handle_click)

    def update_board(self):
        self.canvas.delete("all")
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        square_size = 50
        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "grey"
                self.canvas.create_rectangle(
                    col * square_size,
                    row * square_size,
                    (col + 1) * square_size,
                    (row + 1) * square_size,
                    fill=color
                )

    def get_image_url(self, piece):
        piece_images = [
            "pawn.png",
            "knight.png",
            "bishop.png",
            "rook.png",
            "queen.png",
            "king.png"
        ]

        if piece.color:
            return "img/white/" + piece_images[piece.piece_type - 1]
        else:
            return "img/black/" + piece_images[piece.piece_type - 1] 
        

    def draw_pieces(self):
        self.image_references = []

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                piece_image = Image.open(self.get_image_url(piece))
                piece_image = piece_image.resize((50, 50))
                piece_image = ImageTk.PhotoImage(piece_image)
                self.image_references.append(piece_image)
                self.canvas.create_image(
                    chess.square_file(square) * 50 + 25,
                    (7 - chess.square_rank(square)) * 50 + 25,
                    anchor=tk.CENTER,
                    image=piece_image
                )
        

    def handle_click(self, event):
        # TODO select piece -> select move
        col = event.x // 50
        row = 7 - (event.y // 50)
        clicked_square = chess.square(col, row)
        # print(f"click detected at col {col}, row {row} \n this is square {clicked_square}")
        legal_moves = list(self.board.legal_moves)
        legal_squares = [move.to_square for move in legal_moves]

        if clicked_square in legal_squares:
            move = [str(move) for move in legal_moves if move.to_square == clicked_square][0]
            self.do_move(chess.Move.from_uci(move))
            # sounds.play_move()
            self.do_move(self.controller.get_ai_move())

    def do_move(self, move):
        self.board.push(move)
        self.update_board()

    def set_controller(self, controller):
        self.controller = controller


def main():
    root = tk.Tk()
    chess_gui = ChessGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
