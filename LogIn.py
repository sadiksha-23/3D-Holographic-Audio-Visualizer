from customtkinter import *
from PIL import Image
import os
from functions import *

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to build the login interface
def build_login_frame(frame, show_frame, frames):
    # Load visual assets
    side_img = CTkImage(dark_image=Image.open("images/hologram.jpg"), size=(300, 480))
    email_icon = CTkImage(dark_image=Image.open("images/email-icon.png"), size=(20, 20))
    password_icon = CTkImage(dark_image=Image.open("images/password-icon.png"), size=(17, 17))

    # Add side image panel
    CTkLabel(master=frame, text="", image=side_img).pack(expand=True, side="left")

    # Create right-side form panel for login inputs
    form = CTkFrame(master=frame, width=300, height=480)
    form.pack_propagate(0)  # Prevents form from shrinking to widget size
    form.pack(expand=True, side="right")

    # Welcome header
    CTkLabel(master=form, text="Welcome Back!", text_color="#601E88", anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=form, text="Log in to your account", text_color="#7E7E7E", anchor="w", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    # Email field
    CTkLabel(master=form, text="  Email:", text_color="#601E88", anchor="w", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    email_entry = CTkEntry(master=form, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
    email_entry.pack(anchor="w", padx=(25, 0))

    # Password field
    CTkLabel(master=form, text="  Password:", text_color="#601E88", anchor="w", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    password_entry = CTkEntry(master=form, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
    password_entry.pack(anchor="w", padx=(25, 0))

    # Label to display login errors
    error_label = CTkLabel(master=form, text="", text_color="black", font=("Arial", 11))
    error_label.pack(anchor="w", padx=(25, 0), pady=(10, 0))

    # Handle login logic
    def handle_login():
        email = email_entry.get()
        password = password_entry.get()
        if authenticate_user(email, password):  # Check credentials
            error_label.configure(text="")  # Clear error
            show_frame(frames["homepage"])  # Navigate to homepage
        else:
            error_label.configure(text="Invalid email or password")  # Show error

    # Login button
    CTkButton(master=form, text="Login", command=handle_login, fg_color="#601E88", hover_color="#E44982",
              font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))

    # Button to switch to the signup page
    CTkButton(master=form, text="Sign Up", command=lambda: show_frame(frames["signup"]), fg_color="#EEEEEE",
              hover_color="#D3D3D3", font=("Arial Bold", 12), text_color="#601E88", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))
