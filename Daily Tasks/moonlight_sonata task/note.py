from dataclasses import dataclass


@dataclass(frozen=True)
class Note:
    pitch: str | int
    duration: float
    velocity: int = 64
