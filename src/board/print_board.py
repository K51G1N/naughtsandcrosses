def print_board(board):
    """
    receives the mapped board and prints it to the screen
    Args:
        board (list): Contains X's and O's where the user has placed them 
    """
    content = f"""
          {board[0]} | {board[1]} | {board[2]}
         --- --- ---
          {board[3]} | {board[4]} | {board[5]}
         --- --- ---
          {board[6]} | {board[7]} | {board[8]}
"""
    print(content)