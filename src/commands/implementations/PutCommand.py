from src.Tile import Tile
from src.Player import Player
from src.commands.Execution import Execution
from src.commands.Command import Command
from src.const import ABRV_TO_COLOR
from src.helper.type_helper import args_to_right_type
from src.utils.tile_name_to_tile import tile_name_to_tile


class PutCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        if len(execution.command_args) < 2:
            return False, "Not enough arguments for put command. <set id> <tile name> <position> (default to last)"
        if len(execution.command_args) < 3:
            execution.command_args.append("-1")

        status, conv_command_args = args_to_right_type(execution.command_args, [int, str, int])
        if not status:
            return False, f"You did not gave the right type for argument {len(conv_command_args)}"

        set_id, tile_name, position = conv_command_args
        b, tile = tile_name_to_tile(tile_name)
        if not b:
            return False, f"Tile {tile_name} does not exist"
        if set_id < 0 or set_id > len(execution.game.board.tilesets)-1:
            return False, f"'{set_id}' is not a valid set id."


        if position > len(execution.game.board.tilesets[set_id])-1:
            return   False, f"Position {position} is out of bounds for set {set_id}."

        if not self.player_has_tile(execution.game.current_player, tile):
            return False, f"You do not have the tile: {tile.colorize()}"

        wntd_tileset = execution.game.board.tilesets[set_id]
        self.remove_tile_from_player(execution.game.current_player, tile)
        wntd_tileset.add_tile_to(tile, position)

        return True, f"Tile {tile.colorize()} put into set {set_id} at position {position}."

    @staticmethod
    def player_has_tile(p: Player, t: Tile) -> bool:
        if t in p.tiles_cache:
            return True
        if p.inventory.contains(t):
            return True
        return False

    @staticmethod
    def remove_tile_from_player(player, tile):
        if tile in player.tiles_cache:
            player.tiles_cache.remove(tile)
            return
        if player.inventory.contains(tile):
            player.inventory.remove(tile)
