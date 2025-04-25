from customtkinter import *
import os
from functions import *

# Set working directory to the script's location to ensure relative file paths work correctly
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize the main CustomTkinter application window
app = CTk()
app.geometry("600x480")  # Set the default window size

# Main container to hold all page frames
main_container = CTkFrame(app)
main_container.pack(fill="both", expand=True)

# Create individual frames for each section/page of the app
login_frame = CTkFrame(main_container)
login_frame._name = "login"  # Name helps identify the frame when switching

signup_frame = CTkFrame(main_container)
signup_frame._name = "signup"

homepage_frame = CTkFrame(main_container)
homepage_frame._name = "homepage"

settings_page = CTkFrame(main_container)
settings_page._name = "settingpage"

# Store all frames in a dictionary for easy reference
frames = {
    "login": login_frame,
    "signup": signup_frame,
    "homepage": homepage_frame,
    "settingpage": settings_page
}

# Function to show a specific frame and hide the others
def show_frame(frame):
    for widget in main_container.winfo_children():
        widget.pack_forget()  # Hide all frames
    frame.pack(fill="both", expand=True)  # Show selected frame

    # If the frame has a 'refresh' method (like homepage), call it
    if hasattr(frame, "refresh"):
        frame.refresh()

# Import page builder functions from their respective files
from LogIn import build_login_frame
from SignUp import build_signup_frame
from HomePage import build_homepage_frame
from settings import build_settings_frame

# Build each frame and pass necessary references for navigation
build_login_frame(login_frame, show_frame, frames)
build_signup_frame(signup_frame, show_frame, frames)
build_homepage_frame(homepage_frame, show_frame, frames)
build_settings_frame(settings_page, show_frame, frames)

# Set the login page as the first screen shown on app start
show_frame(login_frame)

# Start the application event loop
app.mainloop()
