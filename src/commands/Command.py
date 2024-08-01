from src.commands.Execution import Execution

class Command:
    def __init__(self, name: str, description: str="No description provided."):
        self.name: str = name
        self.description: str = description

    def execute(self, execution: Execution) -> tuple[bool, str]:
        raise NotImplementedError

    @staticmethod
    def has_valid_args(args: list[str], min_args: int = 3) -> bool:
        return len(args) >= min_args
