from src.commands.Command import Command
from src.const import ABRV_TO_COLOR
from src.Tile import Tile
from src.Tileset import Tileset
from src.commands.Execution import Execution
from src.utils.tile_name_to_tile import tile_name_to_tile

class CreateCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        if not self.has_valid_args(execution.command_args, 3):
            return False, "Not enough arguments for create command."

        success, split_tiles = self.split_tiles(execution.command_args)
        if not success:
            return False, f"Tile {execution.command_args[len(split_tiles)]} does not exist."

        missing_tiles = self.get_missing_tiles(execution.game.current_player, split_tiles)
        if missing_tiles:
            return False, f"You miss the following tiles: {' '.join(t.colorize() for t in missing_tiles)}"

        tileset_instance = self.create_tileset(split_tiles)
        if not tileset_instance:
            return False, f"Invalid tileset. {' '.join(t.colorize() for t in split_tiles)}"

        execution.game.board.add_tileset(tileset_instance)
        self.remove_tiles_from_inventory(execution.game.current_player, split_tiles)

        return True, f"Tileset created with tiles: {' '.join(t.colorize() for t in split_tiles)}."


    def split_tiles(self, tile_strings: list[str]) -> tuple[bool, list[Tile]]:
        tiles = []
        for tile_string in tile_strings:
            success, tile = tile_name_to_tile(tile_string)
            if not success:
                return False, tiles
            tiles.append(tile)
        return True, tiles

    @staticmethod
    def create_tileset(tiles: list[Tile]) -> Tileset | None:
        tileset = Tileset(tiles=tiles)
        return tileset if tileset.is_valid() else None

    @staticmethod
    def player_has_all_tiles(player, tiles: list[Tile]) -> bool:
        return all(tile in player.tiles_cache or player.inventory.contains(tile) for tile in tiles)

    @staticmethod
    def get_missing_tiles(player, tiles: list[Tile]) -> list[Tile]:
        return [tile for tile in tiles if tile not in player.tiles_cache and not player.inventory.contains(tile)]

    @staticmethod
    def remove_tiles_from_inventory(player, tiles: list[Tile]):
        for tile in tiles:
            if tile in player.tiles_cache:
                player.tiles_cache.remove(tile)
            elif player.inventory.contains(tile):
                player.inventory.remove(tile)
