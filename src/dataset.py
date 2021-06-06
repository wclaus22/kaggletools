from pathlib import Path

from abc import ABC, abstractmethod


class BaseDataset(ABC):
    def __init__(self, path):
        self._path = path
        self._path_elements = [item for item in Path(path).iterdir()]

    @abstractmethod
    def __getitem__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass