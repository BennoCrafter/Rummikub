from src.tileset import Tileset
from src.tile import Tile


class PlayerInventory(Tileset):
    def __init__(self, tiles: list[Tile]) -> None:
        super().__init__(tiles)

    def __str__(self) -> str:
        return self.colorize()

    def colorize(self) -> str:
        return " ".join(t.colorize() for t in self.tiles)
