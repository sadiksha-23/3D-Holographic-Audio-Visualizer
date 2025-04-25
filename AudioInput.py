import numpy as np
import sounddevice as sd

# Class to capture real-time audio input and calculate its energy
class AudioInput:
    def __init__(self):
        self.energy = 0.0  # Stores current audio energy level
        # Initialize the input audio stream and link it to the callback
        self._stream = sd.InputStream(callback=self._audio_callback)

    # Start capturing audio
    def start(self):
        self._stream.start()

    # Stop capturing audio
    def stop(self):
        self._stream.stop()

    # Callback function that gets called automatically with each audio frame
    def _audio_callback(self, indata, frames, time, status):
        # Calculate root mean square (RMS) energy from input data
        self.energy = np.sqrt(np.mean(indata**2))

    # Retrieve the latest calculated energy value
    def get_energy(self):
        return self.energy
