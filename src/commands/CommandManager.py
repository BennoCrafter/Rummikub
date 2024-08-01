from src.commands.Execution import Execution
from src.Player import Player
from src.commands.Command import Command

class CommandManager:
    def __init__(self, cmd_repo=[]):
        self.commands: dict = {}

        for cmd_cls in cmd_repo:
            self.register_command(cmd_cls)

    # command attr is a subclass of Command (cant find a way to type hint this)
    def register_command(self, command):
        self.commands[command.name] = command

    def execute_command(self, game, user_input: str) -> tuple[bool, str]:
        parts: list = user_input.split()
        if not parts:
            return False, "No command provided."

        command_name: str = parts[0]
        # args are the remaining parts of the input from index 1 to the end
        args: list = parts[1:]
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
