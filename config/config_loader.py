import yaml

class ConfigLoader:
    _instance = None

    def __new__(cls, file_path='config/config.yaml') :
        if cls._instance is None:
            cls._instance = super(ConfigLoader, cls).__new__(cls)
            cls._instance._load_config(file_path)
        return cls._instance

    def _load_config(self, file_path):
        with open(file_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_config(self):
        return self.config

def get_config(file_path='config/config.yaml'):
    return ConfigLoader(file_path).get_config()
