# commands.py
from customtkinter import *
import os

# Set working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize app
app = CTk()
app.geometry("600x480")

# Main container frame
main_container = CTkFrame(app)
main_container.pack(fill="both", expand=True)

# Create named page frames
login_frame = CTkFrame(main_container)
login_frame._name = "login"
signup_frame = CTkFrame(main_container)
signup_frame._name = "signup"

# Store frames in a dictionary
frames = {
    "login": login_frame,
    "signup": signup_frame
}

# Frame switch function
def show_frame(frame):
    for widget in main_container.winfo_children():
        widget.pack_forget()
    frame.pack(fill="both", expand=True)

# Import builders after defining frames
from LogIn import build_login_frame
from SignUp import build_signup_frame

# Populate frames
build_login_frame(login_frame, show_frame, frames)
build_signup_frame(signup_frame, show_frame, frames)

# Show login by default
show_frame(login_frame)

# Run the app
app.mainloop()