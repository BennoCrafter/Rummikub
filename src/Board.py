from src.Pool import Pool
from src.Tile import Tile
from src.Tileset import Tileset
from src.commands.CommandManager import CommandManager

from src.commands.implementations import *

class Board:
    def __init__(self, tilesets: list[Tileset]=[], pool=Pool()) -> None:
        self.tilesets: list[Tileset] = tilesets
        self.pool = pool

    def __str__(self) -> str:
        return self.prettify_board()

    def prettify_board(self) -> str:
        out = ''
        for index, tileset in enumerate(self.tilesets):
            out += f'Set {index}:'
            for tile in tileset.tiles:
                out += f' {tile.colorize()}'
            out += '\n'
        return out

    def is_valid(self) -> bool:
        for tileset in self.tilesets:
            if not tileset.is_valid():
                return False
        return True

    def get_tileset_by_id(self, wnt_id: int) -> Tileset:
        return self.tilesets[wnt_id]

    def add_tileset(self, tileset: Tileset) -> None:
        self.tilesets.append(tileset)

    def create_tileset(self, tiles: list[Tile]) -> None:
        self.tilesets.append(Tileset(tiles))

    def get_random_tile(self) -> Tile:
        return self.pool.get_random_tile()
