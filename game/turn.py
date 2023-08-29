from src.board.print_board import print_board
from src.clear import clear_screen

from game.validate_cell_selection import validate_cell_selection
from game.logic import logic

def turn(game_board, player):
    """
    This represents a players turn and the mark they make on the grid is captured
    """
    mapping = {-1: "X", 0: " ", 1: "O"}
    mapped_board = [mapping[cell] for cell in game_board.board]
    clear_screen()
    print_board(mapped_board)
    print(f"It's your turn {player.name} Choose a valid cell to mark 1-9")
    invalid = True
    while invalid:
        try:
            cell_chosen = (int(input()) - 1)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        if not (0 <= cell_chosen < 9):
            print("Invalid cell number! Please choose a number between 1 and 9.")
            continue
        if validate_cell_selection(cell_chosen, game_board):
            print("Cell is already occupied! Please choose an empty cell.")
            continue
        invalid = False
    player.mark(cell_chosen, game_board)
    mapped_board = [mapping[cell] for cell in game_board.board]
    state = logic(game_board)
    return state, mapped_board