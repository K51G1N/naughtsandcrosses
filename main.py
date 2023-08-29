"""
This is the main entry point for our game

"""

from src.welcome.welcome import welcome
from game.setup import setup_game

def main():
    """
    Gets the game started
    """
    welcome()
    setup_game() 

if __name__ == "__main__":
    main()