class Board():
    """
    Represents a grid of naughts and crosses for a game.

    """
    def __init__(self):
        """
        Initializes the grid with empty slots
        """
        self.board = [0] * 9
        self.free_slots = 9

    def mark(self, cell, symbol):
        """
        This marks the board with the respective players symbol in the specified cell
        
        Args:
            cell (int): Postion the player is making a mark
        
        """        
        self.board[cell] = symbol
        self.free_slots -= 1

