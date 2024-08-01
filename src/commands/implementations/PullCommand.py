from src.Tile import Tile
from src.commands.Execution import Execution
from src.commands.Command import Command
from src.const import ABRV_TO_COLOR
from src.helper.type_helper import args_to_right_type
from src.utils.tile_name_to_tile import tile_name_to_tile


class PullCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        if len(execution.command_args) < 2:
            return False, "Not enough arguments for pull command. <set id> <tile name>"
        status, conv_command_args = args_to_right_type(execution.command_args, [int, str])
        if not status:
            return False, f"You did not gave the right type for argument {len(conv_command_args)}"

        set_id, tile_name = conv_command_args

        if set_id < 0 or set_id > len(execution.game.board.tilesets)-1:
            return False, f"'{set_id}' is not a valid set id."

        wntd_tileset = execution.game.board.tilesets[set_id]
        b, tile = tile_name_to_tile(tile_name)
        if not b:
            return False, f"Tile {tile_name} does not exist"

        if wntd_tileset.contains(tile):
            wntd_tileset.remove(tile)
            if not wntd_tileset:
                # if tileset empty remove it from board
                execution.game.board.tilesets.remove(wntd_tileset)
            execution.game.current_player.add_tile_to_cache(tile)

        return True, f"Tile {tile.colorize()} pulled from set {set_id}."
