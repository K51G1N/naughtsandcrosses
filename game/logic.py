def logic(game_board):
    """
    This module checks the game state  win (rows, diagonals, columns) or draw and then returns the state

    Args:
        game_board (Board): An instance of the game board
    """
    state = ""
    if abs(game_board.board[0] + game_board.board[1] + game_board.board[2]) == 3:
        state = "Winner"
    elif abs(game_board.board[3] + game_board.board[4] + game_board.board[5]) == 3:
        state = "Winner"
    elif abs(game_board.board[6] + game_board.board[7] + game_board.board[8]) == 3:
        state = "Winner"
    elif abs(game_board.board[0] + game_board.board[4] + game_board.board[8]) == 3:
        state = "Winner"
    elif abs(game_board.board[2] + game_board.board[4] + game_board.board[6]) == 3:
        state = "Winner"
    elif abs(game_board.board[0] + game_board.board[3] + game_board.board[6]) == 3:
        state = "Winner"
    elif abs(game_board.board[1] + game_board.board[4] + game_board.board[7]) == 3:
        state = "Winner"
    elif abs(game_board.board[2] + game_board.board[5] + game_board.board[8]) == 3:
        state = "Winner"
    elif game_board.free_slots == 0:
        state = "Draw"
    return state