from src.commands.command import Command
from src.commands.execution import Execution


class NextCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        success, response = execution.game.handle_next_command()
        return success, f"{response}"
