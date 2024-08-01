import readline
from importlib import util

if not util.find_spec("readline"):
    print("Module readline not available on this machine.")

from src.const import COLOR_CODES
from src.Board import Board
from src.Player import Player
from src.Bot import Bot
from src.PlayerInventory import PlayerInventory
from src.Tileset import Tileset
from src.Tile import Tile
from src.commands.CommandManager import CommandManager
from src.commands.implementations import *
from config.config_loader import get_config


class Game:
    def __init__(self, players=None):
        if players is None:
            players = []
        self.config = get_config()
        self.players: list[Player] = players
        self.board: Board = Board()
        self.running: bool = True
        self.command_manager: CommandManager = self.initialize_command_manager()
        self.current_player: Player

    def initialize_command_manager(self) -> CommandManager:
        commands = [
            DrawCommand("draw", "Draw a tile from the pool"),
            PullCommand("pull", "Pull a tile from a tileset. Usage: pull <tileset_id> <tile_name>"),
            PutCommand("put", "Put a tile from your inventory to a tileset. Usage: put <tileset_id> <tile_name>"),
            CreateCommand("create", "Create a new tileset. Usage: create <tile_name> <tile_name> ..."),
            SplitCommand("split", "Split a tileset. Usage: split <tileset_id> <position>"),
            HelpCommand("help", "Display the help message"),
            NextCommand("next", "End your turn"),
            QuitCommand("quit", "Quit the game"),
        ]
        if self.config["rules"]["cheat_command_enabled"]:
            commands.append(CheatCommand("cheat"))
        return CommandManager(commands)

    def init_game(self) -> None:
        if not self.players:
            raise ValueError("No players registered.")
        self.current_player = self.players[0]
        self.display_turn_message()
        self.print_tui()

    def display_turn_message(self) -> None:
        print(f"{COLOR_CODES['blue']}It's your turn: {self.current_player.name}{COLOR_CODES['reset']}")

    def print_tui(self) -> None:
        print(self.board)
        print(f"{COLOR_CODES['green']}Your ({self.current_player}) inventory: \n{self.current_player.inventory}{COLOR_CODES['reset']}")

    def check_win(self) -> None:
        if self.current_player.has_won():
            print(f"{COLOR_CODES['green']}Congratulations {self.current_player.name}! You won the game!{COLOR_CODES['reset']}")
            self.running = False
            exit(0)

    def game_loop(self) -> None:
        self.init_game()
        try:
            while self.running:
                self.process_turn()
        except KeyboardInterrupt:
            print("quit\nGame stopped.")
            exit(0)

    def process_turn(self) -> None:
        if self.current_player.tiles_cache:
            self.display_tiles_cache()
        cmd_str: str = input("Enter your command: ")
        success, message = self.command_manager.execute_command(self, cmd_str)
        self.handle_command_result(success, message)

    def display_tiles_cache(self) -> None:
        print(f"Your tiles cache: {' '.join(t.colorize() for t in self.current_player.tiles_cache)}")

    def handle_command_result(self, success: bool, message: str):
        command = message
        self.print_tui()
        self.display_command_result(success, message)

    def handle_next_command(self) -> tuple[bool, str]:
        if not self.board.is_valid():
            return False, f"{COLOR_CODES['red']}Invalid board state.{COLOR_CODES['reset']}"
        if not self.current_player.tiles_cache_is_empty():
            return False, f"{COLOR_CODES['red']}Your tiles cache is not empty!{COLOR_CODES['reset']}"
        self.check_win()
        self.next_player()
        return True, ""

    def display_command_result(self, success: bool, message: str):
        color = COLOR_CODES["green"] if success else COLOR_CODES["red"]
        print(f"\n{color}{message}{COLOR_CODES['reset']}")

    def register_player(self, player_name: str) -> None:
        self.players.append(Player(player_name, PlayerInventory(self.board.pool.generate_pool_for_player())))

    def register_bot(self, bot_name: str) -> None:
        self.players.append(Bot(bot_name, PlayerInventory(self.board.pool.generate_pool_for_player())))

    def next_player(self) -> None:
        self.players.append(self.players.pop(0))
        self.current_player = self.players[0]
        self.display_turn_message()
        if self.current_player.is_bot:
            success, msg = self.current_player.make_move(self.board)
            if not success:
                self.throw_error(msg)

    def rollback(self):
        pass

    def throw_error(self, msg: str, is_critical: bool=False) -> None:
        print(f"Error: {msg}")
        if is_critical:
            exit(1)

# Example usage
if __name__ == "__main__":
    def call_example():
        board_tiles = [
            Tileset([Tile("red", 3), Tile("yellow", 3), Tile("blue", 3)]),
            Tileset([Tile("red", 2), Tile("red", 3), Tile("red", 4), Tile("red", 5)]),
        ]
        game.board = Board(tilesets=board_tiles)

    game = Game()
    game.register_player("Player1")
    game.register_player("Player2")
    call_example()
    game.game_loop()
