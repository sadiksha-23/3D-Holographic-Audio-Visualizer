How to Run This Project
This project is built with Python and requires a few external libraries to run. Follow these steps to get the 3D Holographic Audio Visualizer working on your local machine.

1. Prerequisites

Python 3.7 or higher installed on your system.
A default microphone or an external microphone connected to your computer for audio input.

2. Clone the Repository

First, clone this repository to your local machine using git:
git clone https://github.com/sadiksha-23/3D-Holographic-Audio-Visualizer

3. Install Dependencies
This project uses several Python libraries. Run the following command in your terminal to install them all at once:
pip install pygame sounddevice numpy customtkinter 

4. Run the Application (Two-Window Setup)
This project is designed to run in two separate windows simultaneously on the same device: one for the control dashboard and one for the visualizer.

   Step A: Start the Visualizer
   Open a terminal or command prompt window.
   Navigate to the project directory.
   Run the visualgeneration.py script. This will open a Pygame window which will display the visuals:
   python visualgeneration.py

   Step B: Start the Controller
   Open a second, new terminal or command prompt window. (Keep the first one running).
   Navigate to the same project directory.
   Run the commands.py script. This will launch the GUI dashboard:
   python commands.py

Now, you will have two windows open. The GUI dashboard from commands.py will control the graphics being rendered in the visualgeneration.py window in real-time. Enjoy the show!
