from os import system

import time
import random
import chess
from boardstate import state
from game_algorithm import minimaxAB_player
from board import creature, generate_board, clear_board

''' Basic mechanics of the game. This file calls differnet functions which help generating the board and playing the game.
Adds time and also shows messages if game is won/stalemate/draw '''

def play_chess(player1, player2, visual='simple', pause=0.1):

    board = chess.Board()

    while not board.is_game_over(claim_draw= True):
        start_time = time.time()
        if board.uci == chess.WHITE:
            uci = player1(board)
        else:
            uci = player2(board)
        time_elapsed = time.time() - start_time

        name = creature(board.uci)
        board.push_turn(uci)
        board_stop = generate_board(board)
        move_info = "Move %s %s, Play '%s' in %s seconds\n%s" % (
                        len(board.move_stack), name, uci, str(time_elapsed), board_stop)

        if visual is not None:
            clear_board()
            print(move_info)
            time.sleep(pause)


    result = None
    if board.is_checkmate():
        msg = "checkmate: " + creature(not board.uci) + " wins!"
        result = not board.uci
    elif board.is_stalemate():
        msg = "draw: stalemate"
    elif board.is_fivefold_repetition():
        msg = "draw: 5-fold repetition"
    elif board.is_insufficient_material():
        msg = "draw: insufficient material"
    elif board.can_claim_draw():
        msg = "draw: claim"
    if visual is not None:
        print(msg)
    
    return (result, msg, board)                        


if __name__ == "__main__":
    play_chess(minimaxAB_player,minimaxAB_player,visual='simple',pause=0.1)

    
    


