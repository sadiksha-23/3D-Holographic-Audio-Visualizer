import pyaudio
import numpy as np
import os
import time

# Audio settings

FORMAT = pyaudio.paFloat32  # Format for the audio data (32-bit floating point)
CHANNELS = 1  # Single channel audio (mono)
RATE = 44100  # Sample rate (samples per second)
CHUNK = 16384  # Size of each audio chunk (how many samples to read at once)
ENERGY_THRESHOLD = 0.035  # Threshold for audio energy to detect a "beat" (adjustable)

# Initialize PyAudio
p = pyaudio.PyAudio()  # Create a PyAudio object for capturing live audio.

# Open audio stream from USB microphone
stream = p.open(
    format=FORMAT,        # Set the format for audio data to be captured
    channels=CHANNELS,    # Set to mono (single channel)
    rate=RATE,            # Set the sample rate to 44100
    input=True,           # Enable audio input (from microphone)
    frames_per_buffer=CHUNK  # Number of frames per buffer (each chunk)
)

# Inform that the program is listening for audio
print("Listening for beats...")

try:
    # Main loop to keep listening to the audio stream
    while True:
        # Read audio data from the stream (the input audio buffer)
        data = stream.read(CHUNK, exception_on_overflow=False)
        
        # Convert the raw audio data to a numpy array (32-bit floats)
        audio = np.frombuffer(data, dtype=np.float32)

        # Calculate the energy of the audio signal
        energy = np.sqrt(np.mean(audio**2))  

        # Print the current energy value (for debugging or monitoring)
        print(f"Energy: {energy:.5f}")

        # If the energy exceeds the set threshold, we consider it a "beat"
        if energy > ENERGY_THRESHOLD:
            print("🎵 Beat detected!")  # Print when a beat is detected

            # Trigger to run a script on the Raspberry Pi via SSH
            os.system("ssh pi@192.168.1.94 \"bash -lc 'python3 /home/pi/test.py'\"")

        else:
            print("No beat detected.")  # Print if no beat is detected (energy is below the threshold)

# Handling interruption 
except KeyboardInterrupt:
    print("Stopping...")  # Print when the program is interrupted
    stream.stop_stream()  # Stop the audio stream
    stream.close()  # Close the audio stream
    p.terminate()  # Terminate the PyAudio instance
