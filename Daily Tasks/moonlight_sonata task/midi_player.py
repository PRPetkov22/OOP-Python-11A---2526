from pathlib import Path
import time

from AVFoundation import AVMIDIPlayer
from Foundation import NSURL

from player import Player


class MidiPlayer(Player):
    def __init__(self) -> None:
        self.player = None

    def play(self, path: str | Path) -> None:
        midi_url = NSURL.fileURLWithPath_(str(Path(path).resolve()))
        bank_url = NSURL.fileURLWithPath_(
            "/System/Library/Components/CoreAudio.component/Contents/Resources/gs_instruments.dls"
        )
        self.player, error = AVMIDIPlayer.alloc().initWithContentsOfURL_soundBankURL_error_(midi_url, bank_url, None)
        if self.player is None:
            raise RuntimeError(f"Неуспешно зареждане на MIDI файла: {error}")
        self.player.prepareToPlay()
        self.player.play_(None)
        time.sleep(self.player.duration())

    def close(self) -> None:
        self.player = None
