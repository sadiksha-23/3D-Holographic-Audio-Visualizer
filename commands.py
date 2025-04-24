from customtkinter import *
import os
from functions import *

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

homepage_frame = CTkFrame(main_container)
homepage_frame._name = "homepage"

settings_page = CTkFrame(main_container)
settings_page._name = "settingpage"

# Store frames in a dictionary
frames = {
    "login": login_frame,
    "signup": signup_frame,
    "homepage": homepage_frame,
    "settingpage": settings_page
}

def show_frame(frame):
    for widget in main_container.winfo_children():
        widget.pack_forget()
    frame.pack(fill="both", expand=True)

    # 🧠 Refresh homepage content if applicable
    if hasattr(frame, "refresh"):
        frame.refresh()

# Import builders
from LogIn import build_login_frame
from SignUp import build_signup_frame
from HomePage import build_homepage_frame
from settings import build_settings_frame

# Populate frames
build_login_frame(login_frame, show_frame, frames)
build_signup_frame(signup_frame, show_frame, frames)
build_homepage_frame(homepage_frame, show_frame, frames)
build_settings_frame(settings_page, show_frame, frames)

# Show login by default
show_frame(login_frame)

# Run the app
app.mainloop()

