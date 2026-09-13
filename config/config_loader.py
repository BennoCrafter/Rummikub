from typing import Any

import yaml

class ConfigLoader:
    _instance = None

    def __new__(cls, file_path: str = 'config/config.yaml') -> "ConfigLoader":
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config(file_path)
        return cls._instance

    def _load_config(self, file_path: str) -> None:
        with open(file_path, 'r') as file:
            self.config: dict[str, Any] = yaml.safe_load(file)

    def get_config(self) -> dict[str, Any]:
        return self.config

def get_config(file_path: str = 'config/config.yaml') -> dict[str, Any]:
    return ConfigLoader(file_path).get_config()
