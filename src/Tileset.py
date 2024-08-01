from src.Tile import Tile

class Tileset:
    """
    This class represents a set of tiles. It provides methods to check the validity of the set,
    determine if the set forms a run or a group, and manipulate the tiles within the set.
    """

    def __init__(self, tiles: list[Tile] = [], type: str = "Tileset") -> None:
        self.tiles: list[Tile] = tiles
        self.type: str = type

    def __len__(self) -> int:
        """Returns the number of tiles in the tileset."""
        return len(self.tiles)

    def __str__(self) -> str:
        """Returns a string representation of the tileset."""
        return " ".join([str(i) for i in self.tiles])

    def check(self) -> str:
        if self.is_consecutive([i.number for i in self.tiles]) and self.has_same([i.color for i in self.tiles]):
            return "run"
        if self.has_same([i.number for i in self.tiles]) and self.has_no_duplicates([i.color for i in self.tiles]):
            return "group"
        return "invalid"

    def is_valid(self) -> bool:
        return self.is_run() or self.is_group()

    def is_run(self) -> bool:
        return self.is_consecutive([i.number for i in self.tiles]) and self.has_same([i.color for i in self.tiles])

    def is_group(self) -> bool:
        return self.has_same([i.number for i in self.tiles]) and self.has_no_duplicates([i.color for i in self.tiles])

    def tile_at(self, position: int) -> Tile:
        return self.tiles[position]

    def contains(self, tile: Tile) -> bool:
        return tile in self.tiles

    def position_of(self, tile: Tile) -> int:
        return self.tiles.index(tile)

    def remove(self, tile: Tile) -> None:
        self.tiles.remove(tile)

    def add_tile_to(self, tile: Tile, position: int) -> None:
        if position == -1:
            self.append(tile)
        else:
            self.tiles.insert(position, tile)

    def append(self, tile: Tile) -> None:
        self.tiles.append(tile)

    @staticmethod
    def succ(a: int, b: int) -> bool:
        return (a + 1 == b) or (a == 13 and b == 1)

    @staticmethod
    def is_consecutive(sequence: list[int]) -> bool:
        for j in range(len(sequence) - 1):
            if sequence[j] == -1 or sequence[j + 1] == -1:
                continue
            if not Tileset.succ(sequence[j], sequence[j + 1]):
                return False
        return True

    @staticmethod
    def has_same(sequence: list[str] | list[int]) -> bool:
        base = sequence[0]
        for element in sequence:
            if base == "joker" or base == -1:
                continue
            if element != base:
                return False
        return True

    @staticmethod
    def has_no_duplicates(sequence: list[str] | list[int]) -> bool:
        return len(set(sequence)) == len(sequence)
