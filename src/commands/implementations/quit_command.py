from src.commands.command import Command
from src.commands.execution import Execution


class QuitCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        print("Game stopped.")
        exit(0)
        return True, "quit"
