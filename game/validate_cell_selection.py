def validate_cell_selection(cell_chosen, game_board):
    """
    This function validates the cell chosen. It must be empty.
    Args:
        cell_chosen (int): The cell chosen to place the players marking
        game_board (array): The array of markings on the board.
    """
    if game_board.board[cell_chosen] == 0:
        return False
    else:
        # print("Invalid cell selected! Please choose an empty cell")
        return True