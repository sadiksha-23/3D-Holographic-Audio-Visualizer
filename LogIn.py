# LogIn.py
from customtkinter import *
from PIL import Image
import os

# Set the working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def build_login_frame(frame, show_frame, frames):
    # Load image files
    side_img = CTkImage(dark_image=Image.open("hologram.jpg"), size=(300, 480))
    email_icon = CTkImage(dark_image=Image.open("email-icon.png"), size=(20, 20))
    password_icon = CTkImage(dark_image=Image.open("password-icon.png"), size=(17, 17))

    # Left-side image
    CTkLabel(master=frame, text="", image=side_img).pack(expand=True, side="left")

    # Right-side form panel
    form = CTkFrame(master=frame, width=300, height=480)
    form.pack_propagate(0)
    form.pack(expand=True, side="right")

    # Welcome texts
    CTkLabel(master=form, text="Welcome Back!", text_color="#601E88", anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=form, text="Sign up to your account", text_color="#7E7E7E", anchor="w", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    # Email input
    CTkLabel(master=form, text="  Email:", text_color="#601E88", anchor="w", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    CTkEntry(master=form, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

    # Password input
    CTkLabel(master=form, text="  Password:", text_color="#601E88", anchor="w", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    CTkEntry(master=form, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

    # Buttons
    CTkButton(master=form, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=form, text="Sign Up", command=lambda: show_frame(frames["signup"]), fg_color="#EEEEEE", hover_color="#D3D3D3", font=("Arial Bold", 12), text_color="#601E88", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))