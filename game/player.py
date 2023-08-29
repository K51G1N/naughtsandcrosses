"""
This module represents a player and it's action to put a mark on the board
"""

class Player():
    """
    Represents a player in the game

    Attributes:
        name (str): The name of the player.
    """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.winner = False
    
    def mark(self, cell, board):
        """
        A player can take a turn by marking the board
        Args:
            cell (int): The cell on the board to be marked
            board (Board): A instance of the board to be marked
        """
        board.mark(cell, self.symbol)
