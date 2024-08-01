from src.commands.Command import Command
from src.commands.Execution import Execution


class QuitCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        print("Game stopped.")
        exit(0)
        return True, f"quit"
