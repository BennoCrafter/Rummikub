from src.Tile import Tile
from src.commands.Command import Command
from src.commands.Execution import Execution
from src.utils.tile_name_to_tile import tile_name_to_tile

class CheatCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        if not self.has_valid_args(execution.command_args, 1):
            return False, "Not enough arguments for cheat command. <tile name>"

        b, t = tile_name_to_tile(execution.command_args[0])
        if not b:
            return False, f"Tile {execution.command_args[0]} does not exist."

        execution.game.current_player.add_tile_to_inventory(t)
        return True, f"Tile {t.colorize()} added to inventory."
