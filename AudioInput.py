import numpy as np
import sounddevice as sd

class AudioInput:
    def __init__(self):
        self.energy = 0.0
        self._stream = sd.InputStream(callback=self._audio_callback)

    def start(self):
        self._stream.start()

    def stop(self):
        self._stream.stop()

    def _audio_callback(self, indata, frames, time, status):
        self.energy = np.sqrt(np.mean(indata**2))

    def get_energy(self):
        return self.energy
