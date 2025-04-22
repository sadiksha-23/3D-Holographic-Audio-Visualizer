# SignUp.py
from customtkinter import *
from PIL import Image
import os

# Set the working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def build_signup_frame(frame, show_frame, frames):
    # Load image files
    side_img = CTkImage(dark_image=Image.open("hologram.jpg"), size=(300, 480))
    email_icon = CTkImage(dark_image=Image.open("email-icon.png"), size=(20, 20))
    password_icon = CTkImage(dark_image=Image.open("password-icon.png"), size=(17, 17))

    # Display left-side image
    CTkLabel(master=frame, text="", image=side_img).pack(expand=True, side="left")

    # Create a frame on the right side for signup elements
    form = CTkFrame(master=frame, width=300, height=480)
    form.pack_propagate(0)
    form.pack(expand=True, side="right")

    # Welcome message
    CTkLabel(master=form, text="Create an Account", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

    # Email input section
    CTkLabel(master=form, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    CTkEntry(master=form, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

    # Create password section
    CTkLabel(master=form, text="  Create Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    CTkEntry(master=form, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

    # Confirm password section
    CTkLabel(master=form, text="  Confirm Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    CTkEntry(master=form, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

    # Sign Up button
    CTkButton(master=form, text="Sign Up", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))

    # Return to login button
    CTkButton(master=form, text="Return to Login", command=lambda: show_frame(frames["login"]), fg_color="#EEEEEE", hover_color="#D3D3D3", font=("Arial Bold", 9), text_color="#601E88", width=225).pack(anchor="w", pady=(5, 20), padx=(25, 0))