from src.const import COLOR_CODES, COLOR_TO_ABRV

class Tile:
    def __init__(self, color: str, number: int) -> None:
        self.color: str = color
        self.number: int = number

    def __str__(self) -> str:
        return f"{self.color},{self.number}"

    def __eq__(self, other) -> bool:
        return isinstance(other, Tile) and self.color == other.color and self.number == other.number

    def __hash__(self) -> int:
        return hash((self.color, self.number))

    def colorize(self) -> str:
        color_code: str = COLOR_CODES.get(self.color, COLOR_CODES['reset'])
        return f"{color_code}{COLOR_TO_ABRV.get(self.color)}{self.number}{COLOR_CODES['reset']}"

    def is_joker(self) -> bool:
        if self.number == -1:
            return True
        return False
