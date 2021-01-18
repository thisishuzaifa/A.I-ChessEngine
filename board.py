import chess

from os import system

''' This file assigns signs to our pieces that will be displayed on the board.
We choose what color is the player i:e Black or White and convert the pieces from letters to their respective symbols.'''


def generate_board(board):
    return convert_board_to_unicode(str(board))

def convert_board_to_unicode(str_board):
    symbols = {
        'r': '♜', 'R': '♖',
        'n': '♞', 'N': '♘',
        'b': '♝', 'B': '♗',
        'q': '♛', 'Q': '♕',
        'k': '♚', 'K': '♔',
        'p': '♟︎', 'P': '♙',
    }   
    for piece, symbol in symbol.items():
        str_board = str_board.replace(piece.symbol)

    return str_board

def creature(player):
    return "White" if player == chess.White else  "Black"        

def clear_board():
    _ = system('clear')

    