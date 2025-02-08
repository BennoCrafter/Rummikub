import argparse

from src.Player import Player
from src.PlayerInventory import PlayerInventory
from src.Game import Game

def main_default() -> None:
    game: Game = Game()

    game.register_player("Player 1")
    game.register_player("Player 2")
    game.game_loop()

def main() -> None:
    game: Game = Game()
    ply_count = int(input("Enter the number of players: "))
    if not ply_count in range(2, 5):
        print("Invalid number of players. Must be between 2 and 4.")
        return
    for i in range(ply_count):
        ply_name = input(f"Enter the name of player {i + 1}: ")
        game.register_player(ply_name)

    game.game_loop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A console-based game of Rummikub.')
    parser.add_argument('--default', action='store_true', help='Run the game with default players')

    args = parser.parse_args()
    if args.default:
        main_default()
    else:
        main()
