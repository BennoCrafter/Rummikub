from typing import TYPE_CHECKING

from src.commands.execution import Execution
from src.commands.command import Command

if TYPE_CHECKING:
    from src.game import Game

class CommandManager:
    def __init__(self, cmd_repo: list[Command] = []) -> None:
        self.commands: dict[str, Command] = {}

        for cmd_cls in cmd_repo:
            self.register_command(cmd_cls)

    def register_command(self, command: Command) -> None:
        self.commands[command.name] = command

    def execute_command(self, game: "Game", user_input: str) -> tuple[bool, str]:
        parts: list[str] = user_input.split()
        if not parts:
            return False, "No command provided."

        command_name: str = parts[0]
        # args are the remaining parts of the input from index 1 to the end
        args: list[str] = parts[1:]
        command = self.commands.get(command_name)

        # special case for help command
        if command_name == "help":
            cmd_out = ""
            names = [cmd.name for cmd in self.commands.values()]
            descriptions = [cmd.description for cmd in self.commands.values()]
            for name, description in zip(names, descriptions):
                cmd_out += f"\n{name}:  {description}"
            return True, f"Available commands: {cmd_out}"


        if not command:
            return False, f"Command '{command_name}' not found."

        return command.execute(Execution(args, game))
