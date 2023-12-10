import chess

def get_piece_square_value(piece, square, color):
    piece_type = piece.piece_type
    rank = chess.square_rank(square)
    file = chess.square_file(square)

    # Define base value and positional modifiers
    value_dict = {
        chess.PAWN: {
            "white": {
                2: 0.2,
                7: 0.8,
            },
            "black": {
                1: 0.2,
                6: 0.8,
            },
        },
        chess.KNIGHT: {
            "white": {
                1: 0.3,
                8: 0.3,
                2: 0.2,
                7: 0.2,
            },
            "black": {
                1: 0.3,
                8: 0.3,
                2: 0.2,
                7: 0.2,
            },
        },
        chess.BISHOP: {
            "white": {
                1: 0.2,
                8: 0.2,
                2: 0.1,
                7: 0.1,
            },
            "black": {
                1: 0.2,
                8: 0.2,
                2: 0.1,
                7: 0.1,
            },
        },
        chess.ROOK: {
            "white": {
                1: 0.2,
                8: 0.2,
                4: 0.1,
                5: 0.1,
            },
            "black": {
                1: 0.2,
                8: 0.2,
                4: 0.1,
                5: 0.1,
            },
        },
        chess.QUEEN: {
            "white": {},
            "black": {},
        },
        chess.KING: {
            "white": {},
            "black": {},
        },
    }

    # Apply base value
    base_value = 0

    # Apply positional modifiers based on rank and file
    modifiers = 0
    if color in value_dict[piece_type]:
        for rank_mod, value in value_dict[piece_type][color].items():
            if rank == rank_mod:
                modifiers += value
        for file_mod, value in value_dict[piece_type][color].items():
            if file == file_mod:
                modifiers += value

    return base_value + modifiers

def count_knight_blocked_moves(board, square):
    return 0

def get_piece_activity_score(board):
    score = 0
    for square in chess.scan_reversed(board.occupied):
        piece = board.piece_at(square)
        color = piece.color

        # Count available legal moves for each piece
        legal_moves = list(board.legal_moves)

        # Consider capturing moves as more active
        capturing_moves = [move for move in legal_moves if board.is_capture(move)]
        score += len(capturing_moves) * 0.5

        # Non-capturing moves also contribute to activity
        score += len(legal_moves) * 0.25

        # Penalize pieces with limited mobility due to pawn blocks
        if piece.piece_type == chess.KNIGHT:
            
            blocked_moves = count_knight_blocked_moves(board, square)
            score -= blocked_moves * 0.1

    return score

def get_pawn_structure_score(board):
    return 0

def get_king_safety_score(board):
    return 0

def get_key_squares_score(board):
    return 0


def evaluate(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    material_score = 0
    for square in chess.scan_reversed(board.occupied):
        piece = board.piece_at(square)
        piece_value = piece_values[piece.piece_type]

        if piece.color == chess.WHITE:
            piece_value += get_piece_square_value(piece, square, color="white")
        else:
            piece_value -= get_piece_square_value(piece, square, color="black")

        material_score += piece_value

    # Pawn structure score
    pawn_structure_score = get_pawn_structure_score(board)

    # Piece activity score
    piece_activity_score = get_piece_activity_score(board)

    # Control of key squares score
    key_squares_score = get_key_squares_score(board)

    # King safety score
    king_safety_score = get_king_safety_score(board)

    # Combine all scores with weights
    total_score = (
        material_score +
        0.1 * pawn_structure_score +
        0.35 * piece_activity_score +
        0.1 * key_squares_score +
        0.25 * king_safety_score
    )

    return total_score