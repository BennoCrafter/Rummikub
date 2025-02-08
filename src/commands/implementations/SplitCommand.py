from src.Tile import Tile
from src.commands.Execution import Execution
from src.commands.Command import Command
from src.helper.type_helper import args_to_right_type


class SplitCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        if len(execution.command_args) < 2:
            return False, "Not enough arguments for put command. <set id> <position>"

        status, conv_command_args = args_to_right_type(execution.command_args, [int, int])
        if not status:
            return False, f"You did not gave the right type for argument {len(conv_command_args)}"

        set_id, position = conv_command_args

        if set_id < 0 or set_id > len(execution.game.board.tilesets):
            return False, f"'{set_id}' is not a valid set id."

        wntd_tileset = execution.game.board.tilesets[set_id]

        execution.game.board.create_tileset(wntd_tileset.tiles[:position])
        wntd_tileset.tiles = wntd_tileset.tiles[position:]

        return True, f"Tileset split at position {position} from set {set_id}."
