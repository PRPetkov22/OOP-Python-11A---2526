from pathlib import Path

from midi_player import MidiPlayer
from moonlight_sonata import MoonlightSonata
from player import Player
from score import Score


def main() -> None:
    output_path = Path(__file__).with_name("moonlight_sonata.mid")
    score: Score = MoonlightSonata()
    player: Player = MidiPlayer()
    sequence = score.create_sequence()
    midi_path = sequence.save(output_path)
    try:
        player.play(midi_path)
    finally:
        player.close()


if __name__ == "__main__":
    main()
