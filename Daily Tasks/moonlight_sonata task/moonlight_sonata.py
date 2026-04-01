from mido import tick2second

from moonlight_data import NOTE_EVENTS, TEMPO, TICKS_PER_BEAT
from note import Note
from score import Score
from scheduled_note import ScheduledNote


class MoonlightSonata(Score):
    @property
    def tempo(self) -> int:
        return TEMPO

    @property
    def ticks_per_beat(self) -> int:
        return TICKS_PER_BEAT

    def build_notes(self) -> list[ScheduledNote]:
        return [
            ScheduledNote(
                note=Note(
                    pitch=pitch,
                    duration=tick2second(duration_tick, self.ticks_per_beat, self.tempo),
                    velocity=velocity,
                ),
                start=tick2second(start_tick, self.ticks_per_beat, self.tempo),
                channel=channel,
            )
            for start_tick, duration_tick, pitch, velocity, channel in NOTE_EVENTS
        ]
