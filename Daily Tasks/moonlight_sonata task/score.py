from abc import ABC, abstractmethod

from midi_sequence import MidiSequence
from scheduled_note import ScheduledNote


class Score(ABC):
    @property
    @abstractmethod
    def tempo(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def ticks_per_beat(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def build_notes(self) -> list[ScheduledNote]:
        raise NotImplementedError

    def create_sequence(self) -> MidiSequence:
        sequence = MidiSequence(ticks_per_beat=self.ticks_per_beat)
        sequence.set_tempo(self.tempo)
        for scheduled_note in self.build_notes():
            sequence.add_note(scheduled_note)
        return sequence
