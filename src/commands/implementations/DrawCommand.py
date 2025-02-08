from src.commands.Command import Command
from src.commands.Execution import Execution


class DrawCommand(Command):
    def execute(self, execution: Execution) -> tuple[bool, str]:
        execution.game.current_player.add_tile_to_inventory(execution.game.board.get_random_tile())
        success, response = execution.game.handle_next_command()
        return success, response
