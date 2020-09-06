# http://www.codeskulptor.org/#user47_GBrZgEOa2h_8.py

"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui as poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    game_finished = board.check_win()
    if game_finished:
        return SCORES[game_finished], (-1, -1)

    
    my_move = -1 * SCORES[player],(-1, -1)
    moves = board.get_empty_squares()

    for move in moves:
            
        new_board = board.clone()
        new_board.move(move[0], move[1], player)
        
        score = mm_move(new_board, provided.switch_player(player))[0]
        
        
        if SCORES[player] == 1 and score >= my_move[0]:
            my_move = (score, move)
        elif SCORES[player] == -1 and score < my_move[0]:
            my_move = (score, move)
        
        # current score matches desires score (its a win), no need to consider more alternatives
        if score == SCORES[player]:
            break 
        
    return my_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

#provided.play_game(move_wrapper, 1, False)        
