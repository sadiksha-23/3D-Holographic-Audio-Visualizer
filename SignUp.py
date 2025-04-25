from customtkinter import *
from PIL import Image
import os
from functions import *

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to build the sign-up interface
def build_signup_frame(frame, show_frame, frames):
    # Load visual assets (background and icons)
    side_img = CTkImage(dark_image=Image.open("images/hologram.jpg"), size=(300, 480))
    email_icon = CTkImage(dark_image=Image.open("images/email-icon.png"), size=(20, 20))
    password_icon = CTkImage(dark_image=Image.open("images/password-icon.png"), size=(17, 17))

    # Side image on the left
    CTkLabel(master=frame, text="", image=side_img).pack(expand=True, side="left")

    # Right-side form layout
    form = CTkFrame(master=frame, width=300, height=480)
    form.pack_propagate(0)  # Prevent shrinking to fit children
    form.pack(expand=True, side="right")

    # Header
    CTkLabel(form, text="Create an Account", text_color="#601E88", anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

    # Email input field
    CTkLabel(form, text="  Email:", image=email_icon, compound="left", text_color="#601E88", font=("Arial Bold", 14)).pack(anchor="w", pady=(30, 0), padx=(25, 0))
    email_entry = CTkEntry(form, width=225)
    email_entry.pack(anchor="w", padx=(25, 0))

    # Password input field
    CTkLabel(form, text="  Password:", image=password_icon, compound="left", text_color="#601E88", font=("Arial Bold", 14)).pack(anchor="w", pady=(20, 0), padx=(25, 0))
    password_entry = CTkEntry(form, width=225, show="*")
    password_entry.pack(anchor="w", padx=(25, 0))

    # Confirm password field
    CTkLabel(form, text="  Confirm Password:", image=password_icon, compound="left", text_color="#601E88", font=("Arial Bold", 14)).pack(anchor="w", pady=(20, 0), padx=(25, 0))
    confirm_entry = CTkEntry(form, width=225, show="*")
    confirm_entry.pack(anchor="w", padx=(25, 0))

    # Error message label
    error_label = CTkLabel(form, text="", text_color="black", font=("Arial", 11))
    error_label.pack(anchor="w", padx=(25, 0), pady=(10, 0))

    # Function to handle sign-up logic
    def handle_signup():
        email = email_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()

        if not email or not password:
            error_label.configure(text="Fields cannot be empty")
        elif password != confirm:
            error_label.configure(text="Passwords do not match")
        else:
            # Save credentials to a file
            with open("users.txt", "a") as f:
                f.write(f"{email},{password}\n")
            error_label.configure(text="")  # Clear errors
            show_frame(frames["login"])  # Go back to login screen

    # Sign-up button
    CTkButton(form, text="Sign Up", command=handle_signup, fg_color="#601E88", hover_color="#E44982", text_color="white").pack(anchor="w", pady=(30, 0), padx=(25, 0))

    # Back to login button
    CTkButton(form, text="Back to Login", command=lambda: show_frame(frames["login"]), fg_color="#EEEEEE", text_color="#601E88").pack(anchor="w", pady=(15, 0), padx=(25, 0))
