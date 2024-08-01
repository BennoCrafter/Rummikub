from src.Player import Player


class Execution:
    def __init__(self, command_args, game):
        self.command_args: list[str] = command_args
        self.game = game
