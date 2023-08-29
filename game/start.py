"""
This module starts a game 
"""
from game.turn import turn
from src.board.print_board import print_board

def start_game(game_board, players):
    """
    This is the game started and underway. Will loop until a game end condition (win/draw)
    """
    game_over = False
    while game_over is False:
        for player in players:
            state, mapped_board = turn(game_board, player)
            if state == "Winner":
                print_board(mapped_board)
                print(f"Well done {player.name} you won!!!")
                return
            elif state == "Draw":
                print_board(mapped_board)
                print("The game was a draw. Thanks for playing")
                return
            else:
                pass