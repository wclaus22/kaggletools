"""Basic Dataset Template"""
import pathlib
from abc import ABC, abstractmethod

class BaseDataset(ABC):
    
    def __init__(self, path):
        self._Path = pathlib.Path(path)
    
    @abstractmethod
    def __getitem__(self, idx):
        pass
    
    @abstractmethod
    def __len__(self):
        pass