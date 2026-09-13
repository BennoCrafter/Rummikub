from random import shuffle
from typing import Any

from config.config_loader import get_config
from src.tile import Tile


class Pool:
    def __init__(self) -> None:
        self.pool: list[Tile] = []
        self.config: dict[str, Any] = get_config()
        self.count_for_tile: int = 2
        self.generate_pool()

    def __str__(self) -> str:
        return ", ".join([obj.colorize() for obj in self.pool])

    def generate_pool(self) -> None:
        for set in self.config["tiles"]["sets"]:
            for num in range(set["range"][0], set["range"][1] + 1):
                self.pool.extend([Tile(color=set["color"], number=num)] * set["count"])

        # add joker
        if self.config["rules"]["joker_usage"]:
            for i in range(self.config["tiles"]["jokers"]["count"]):
                self.pool.append(Tile(color="joker", number=-1))

        shuffle(self.pool)

    def generate_pool_for_player(self) -> list[Tile]:
        player_tiles: list[Tile] = self.pool[
            : self.config["game"]["initial_tiles_per_player"]
        ]
        self.pool = self.pool[self.config["game"]["initial_tiles_per_player"] :]
        return player_tiles

    def get_random_tile(self) -> Tile:
        if len(self.pool) == 0:
            print("Pool is empty.")
            exit(0)
        return self.pool.pop()


if __name__ == "__main__":
    e_pool = Pool()
