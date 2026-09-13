from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.game import Game


class Execution:
    def __init__(self, command_args: list[str], game: "Game") -> None:
        self.command_args: list[str] = command_args
        self.game: "Game" = game
