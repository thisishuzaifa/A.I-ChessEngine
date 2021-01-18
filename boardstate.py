import random

import chess


def state(board, my_color):
    piece_score= [
        (chess.PAWN, 10), 
        (chess.BISHOP, 30), 
        (chess.KING, 900), 
        (chess.QUEEN, 90), 
        (chess.KNIGHT, 30),
        (chess.ROOK, 50)


    ]

    score = random.random()

    for (piece, score) in piece_score:
        score += len(board.pieces(piece, my_color)) * score
        score -= len(board.pieces(piece, not my_color)) * score
    score += 2000 if board.is_checkmate() else 0
    return score    