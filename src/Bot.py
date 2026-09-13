from typing import TYPE_CHECKING

from src.player_inventory import PlayerInventory
from src.player import Player

if TYPE_CHECKING:
    from src.board import Board

class Bot(Player):
    def __init__(self, name: str, inventory: PlayerInventory) -> None:
        super().__init__(name, inventory)
        self.strategy: str = "normal"
        self.is_bot: bool = True

    def make_move(self, board: "Board") -> tuple[bool, str]:
        if self.strategy != "normal":
            return False, f"Bot {self.name} is using an unknown strategy"
        return True, "next"
