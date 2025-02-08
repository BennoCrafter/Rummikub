from src.commands.Command import Command
from src.commands.Execution import Execution


class HelpCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        return True, "Following commands:\n - create <tile 1> <tile 2> <tile 3> ..\n - pull <set id> <tile name>\n - put <set id> <tile name> <position>\n - split <set id> <position>\n - draw\n - end (Ends the turn of current player)\n - quit\n - help\n - save <filename>\n - load <filename>"
