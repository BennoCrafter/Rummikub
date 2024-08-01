from src.Tile import Tile
from src.PlayerInventory import PlayerInventory

class Player:
    def __init__(self, name: str, inventory: PlayerInventory) -> None:
        self.name: str = name
        self.inventory: PlayerInventory = inventory
        self.tiles_cache: list[Tile] = []
        self.is_bot: bool = False

    def __str__(self) -> str:
        return self.name

    def add_tile_to_cache(self, t: Tile):
        self.tiles_cache.append(t)

    def add_tile_to_inventory(self, t: Tile):
        self.inventory.tiles.append(t)

    def tiles_cache_is_empty(self):
        return len(self.tiles_cache) == 0

    def has_won(self) -> bool:
        return len(self.inventory.tiles) == 0

    def convert_to_tile_obj(self, l: list[str]) -> Tile:
        return Tile(l[0], int(l[0]))

    def make_move(self, board) -> tuple[bool, str]:
        return False, "This action is not allowed."
