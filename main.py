import chess
import numpy as np
from evaluate import *
from search import * 

import os

def limpiar_consola():
    os.system("cls")

limpiar_consola()
board = chess.Board()

while (True):
    
    print(board)
    print("Puntaje:", evaluate(board))
    mov = input("Ingrese su movimiento: ")
    limpiar_consola()
    try:
        move = board.parse_san(mov)
        board.push(move)
    except:
        print("MOVIMIENTO INVÁLIDO")

    if not board.turn:
        pos_moves = list(board.legal_moves)
        # selected_move = pos_moves[np.random.randint(0,len(pos_moves))]
        selected_move = choose_best_move(board, 3)
        board.push(selected_move)
    
    # print(pos_moves)
    print("La IA juega", selected_move.uci())
    

