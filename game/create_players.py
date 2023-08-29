"""
This module creates two players and returns the list of players
"""

from game.player import Player

def create_players():
    """
    This creates two players and then returns the list of players"""
    players = []
    symbol = [-1, 1]
    characters = ['X', 'O']
    for i in range(0, 2):
        print(f"Enter your player {i+1}'s name: ")
        player_name = input()
        print(f"Nice to have you with us {player_name} you're {characters[i]}")
        player = Player(player_name, symbol[i])
        players.append(player)
    return players
