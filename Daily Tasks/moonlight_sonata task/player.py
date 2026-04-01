from abc import ABC, abstractmethod
from pathlib import Path


class Player(ABC):
    @abstractmethod
    def play(self, path: str | Path) -> None:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError
