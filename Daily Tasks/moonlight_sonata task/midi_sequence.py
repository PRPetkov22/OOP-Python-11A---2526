from pathlib import Path

from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo, second2tick, tempo2bpm

from scheduled_note import ScheduledNote


class MidiSequence:
    def __init__(self, bpm: int = 49, ticks_per_beat: int = 480):
        self.bpm = bpm
        self.ticks_per_beat = ticks_per_beat
        self.tempo = bpm2tempo(bpm)
        self.notes: list[ScheduledNote] = []

    def set_tempo(self, tempo: int) -> None:
        self.tempo = tempo
        self.bpm = round(tempo2bpm(tempo))

    def add_note(self, scheduled_note: ScheduledNote) -> None:
        self.notes.append(scheduled_note)

    def save(self, path: str | Path) -> Path:
        midi = MidiFile(ticks_per_beat=self.ticks_per_beat)
        track = MidiTrack()
        midi.tracks.append(track)
        track.append(MetaMessage("set_tempo", tempo=self.tempo, time=0))
        for channel in sorted({scheduled_note.channel for scheduled_note in self.notes}):
            track.append(Message("program_change", program=0, channel=channel, time=0))

        events: list[tuple[float, int, Message]] = []
        for scheduled_note in self.notes:
            pitch = self.note_name_to_midi(scheduled_note.note.pitch)
            note_on = Message(
                "note_on",
                note=pitch,
                velocity=scheduled_note.note.velocity,
                channel=scheduled_note.channel,
                time=0,
            )
            note_off = Message(
                "note_off",
                note=pitch,
                velocity=0,
                channel=scheduled_note.channel,
                time=0,
            )
            events.append((scheduled_note.start, 1, note_on))
            events.append((scheduled_note.start + scheduled_note.note.duration, 0, note_off))

        events.sort(key=lambda item: (item[0], item[1]))

        current_tick = 0
        for event_time, _, message in events:
            event_tick = round(second2tick(event_time, self.ticks_per_beat, self.tempo))
            message.time = max(0, event_tick - current_tick)
            track.append(message)
            current_tick = event_tick

        track.append(MetaMessage("end_of_track", time=0))

        output_path = Path(path)
        midi.save(output_path)
        return output_path

    @staticmethod
    def note_name_to_midi(note_name: str | int) -> int:
        if isinstance(note_name, int):
            return note_name
        base = note_name.strip().upper()
        natural_pitches = {
            "C": 0,
            "D": 2,
            "E": 4,
            "F": 5,
            "G": 7,
            "A": 9,
            "B": 11,
        }
        pitch = base[:-1]
        octave = int(base[-1])
        natural = pitch[0]
        accidental_value = 0
        for accidental in pitch[1:]:
            if accidental == "#":
                accidental_value += 1
            elif accidental == "B":
                accidental_value -= 1
        return (octave + 1) * 12 + natural_pitches[natural] + accidental_value
