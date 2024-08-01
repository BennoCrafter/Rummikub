from src.Tile import Tile
from random import shuffle
from config.config_loader import get_config


class Pool:
    def __init__(self) -> None:
        self.pool: list[Tile] = []
        self.config = get_config()
        self.count_for_tile: int = 2
        self.colors: list[str] = ["red", "yellow", "blue", "green"]
        self.generate_pool()

    def __str__(self) -> str:
        return (", ".join([obj.colorize() for obj in self.pool]))

    def generate_pool(self) -> None:
        for set in self.config["tiles"]["sets"]:
            for num in range(set["range"][0], set["range"][1] + 1):
                self.pool.extend([Tile(color=set["color"], number=num)] * set["count"])
        # add joker
        jokers = self.config["tiles"]["jokers"]
        for i in range(self.config["tiles"]["jokers"]["count"]):
            self.pool.append(Tile(color="joker", number=-1))

        shuffle(self.pool)

    def generate_pool_for_player(self) -> list[Tile]:
        player_tiles: list[Tile] = self.pool[:13]
        self.pool: list[Tile] = self.pool[13:]
        return player_tiles

    def get_random_tile(self) -> Tile:
        if len(self.pool) == 0:
            print("Pool is empty.")
            exit(0)
        return self.pool.pop()


if __name__ == "__main__":
    e_pool = Pool()
