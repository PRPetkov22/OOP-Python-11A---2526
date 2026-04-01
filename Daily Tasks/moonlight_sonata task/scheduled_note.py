from dataclasses import dataclass

from note import Note


@dataclass(frozen=True)
class ScheduledNote:
    note: Note
    start: float
    channel: int = 0
