# audio detection file

"""sudo apt update && sudo apt upgrade -y"""""
# To update packages^^
"""
sudo apt install python3-pip python3-numpy
pip3 install librosa pyaudio opencv-python gpiozero
"""
# To install libraries^^

import pyaudio
import numpy as np
import librosa
from gpiozero import LED # <- GPIOZero: Controls the LED, flashing it when a beat is detected.
import time

# Initialize LED on GPIO pin 18
led = LED(18) # <- To test LED strip 

# Audio settings
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100  # Sample rate
CHUNK = 1024  # Audio buffer size

# Initialize PyAudio
p = pyaudio.PyAudio() # <- PyAudio: Captures live audio from the microphone.

# Open audio stream from USB microphone
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

print("Listening for beats...")

try:
    while True:
        # Read audio data
        data = stream.read(CHUNK)
        audio = np.frombuffer(data, dtype=np.float32)
        
        # Detect beats using librosa
        # Librosa: Analyzes the audio buffer to detect beats in real-time.
        tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=RATE, units='frames')
        
        # Flash LED if a beat is detected
        if len(beat_frames) > 0:
            led.on()
            time.sleep(0.05)  # flash
            led.off()

except KeyboardInterrupt:
    print("Stopping...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    led.off()
