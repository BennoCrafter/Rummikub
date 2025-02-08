from src.PlayerInventory import PlayerInventory
from src.Player import Player

class Bot(Player):
    def __init__(self, name: str, inventory: PlayerInventory):
        super().__init__(name, inventory)
        self.strategy = "normal"
        self.is_bot: bool = True

    def make_move(self, board) -> tuple[bool, str]:
        if self.strategy != "normal":
            return False, f"Bot {self.name} is using an unknown strategy"
        return True, "next"
