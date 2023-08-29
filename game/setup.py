"""
This module setups up the game by initalising the players and the board
"""

from game.board import Board
from game.create_players import create_players
from game.start import start_game

def setup_game():
    """
    This initialises the board
    Creates the two players and then starts the game
    """
    game_board = Board()
    players = create_players()
    start_game(game_board, players)