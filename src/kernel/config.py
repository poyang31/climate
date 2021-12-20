from os.path import isfile
from pathlib import Path
from typing import Any

from jmespath import search
from yaml import load, FullLoader

current_path = Path(__file__).parent.resolve()


class Config:
    PATH = f"{current_path}/../../config.yaml"

    def __init__(self):
        if not isfile(self.PATH):
            raise Exception(f"The config file, `{self.PATH}` was not found.")
        with open(self.PATH, "r") as configfile:
            self._config = load(configfile, Loader=FullLoader)

    def get(self, xpath: str) -> Any:
        return search(xpath, self._config)
