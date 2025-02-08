from src.Tile import Tile
from src.const import ABRV_TO_COLOR

def tile_name_to_tile(tile_name: str) -> tuple[bool, Tile]:
    # validate that first char is a char and the rest is a number
    if not tile_name[0].isalpha() or not tile_name[1:].strip("-").isdigit():
        return False, Tile("", 0)

    color = ABRV_TO_COLOR[tile_name[0].upper()]
    num = tile_name[1:]

    return True, Tile(color, int(num))
