from customtkinter import *
from PIL import Image
import os

# Set working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = CTk()
set_appearance_mode("dark")
app.after(100, lambda: app.state("zoomed"))

# Sidebar
sidebar_frame = CTkFrame(master=app, fg_color="#2A2F4F", width=176, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img = CTkImage(Image.open("logo_icon.png"), size=(90, 90))
CTkLabel(master=sidebar_frame, image=logo_img, text="").pack(pady=(30, 0))
CTkLabel(master=sidebar_frame, text="3D HOLOGRAPHIC\nAUDIO VISUALIZER", font=("Segoe UI", 12, "bold"),
         text_color="white", justify="center").pack(pady=(10, 20))

CTkButton(master=sidebar_frame, image=CTkImage(Image.open("visualizer_icon.png"), size=(20, 20)),
          text="Visualizer", fg_color="transparent", font=("Segoe UI", 14),
          hover_color="#D9A8E3", anchor="w", compound="left").pack(anchor="center", ipady=5, pady=(10, 0))

CTkButton(master=sidebar_frame, image=CTkImage(Image.open("settings_icon.png"), size=(20, 20)),
          text="Settings", fg_color="transparent", font=("Segoe UI", 14),
          hover_color="#D9A8E3", anchor="w", compound="left").pack(anchor="center", ipady=5, pady=(16, 0))

# Main View
main_view = CTkFrame(master=app, fg_color="#917FB3", corner_radius=0)
main_view.pack(side="left", fill="both", expand=True)
main_view.pack_propagate(0)

# Title
title_frame = CTkFrame(master=main_view, fg_color="transparent")
title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))
CTkLabel(master=title_frame, text="Settings", font=("Segoe UI", 28, "bold"), text_color="#E5BEEC").pack(anchor="nw", side="left")

profile_frame = CTkFrame(master=title_frame, fg_color="transparent")
profile_frame.pack(anchor="ne", side="right")
CTkLabel(master=profile_frame, image=CTkImage(Image.open("person_icon.png"), size=(24, 24)), text="").pack(side="left", padx=(0, 5))
CTkLabel(master=profile_frame, text="name", font=("Segoe UI", 16), text_color="#E5BEEC").pack(side="left")

# Settings Content
settings_content = CTkFrame(master=main_view, fg_color="#917FB3")
settings_content.pack(fill="both", expand=True, padx=27, pady=20)
settings_content.grid_columnconfigure((0, 1), weight=1, uniform="a")

# Row 1
input_device_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
input_device_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=15)
CTkLabel(input_device_frame, text="Input Device", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkOptionMenu(input_device_frame, values=["Default Microphone", "External Mic", "Virtual Audio Cable"], width=250).pack(anchor="w", padx=15, pady=(0, 15))

color_mode_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
color_mode_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=15)
CTkLabel(color_mode_frame, text="Color Mode", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkOptionMenu(color_mode_frame, values=["Static", "Gradient", "Hue", "Reactive"], width=250).pack(anchor="w", padx=15, pady=(0, 15))

# Row 2
threshold_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
threshold_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=15)
CTkLabel(threshold_frame, text="Energy Threshold", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkSlider(threshold_frame, from_=0, to=1, number_of_steps=100, width=250).pack(anchor="w", padx=15, pady=(0, 15))

hue_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
hue_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=15)
CTkLabel(hue_frame, text="Hue Angle (°)", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkSlider(hue_frame, from_=0, to=360, number_of_steps=36, width=250).pack(anchor="w", padx=15, pady=(0, 15))

# Row 3
speed_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
speed_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=15)
CTkLabel(speed_frame, text="Animation Speed", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkSlider(speed_frame, from_=0.1, to=2.0, number_of_steps=20, width=250).pack(anchor="w", padx=15, pady=(0, 15))

detail_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
detail_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=15)
CTkLabel(detail_frame, text="Detail Level", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkOptionMenu(detail_frame, values=["Low", "Medium", "High"], width=250).pack(anchor="w", padx=15, pady=(0, 15))

# Row 4
shape_mode_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
shape_mode_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=15)
CTkLabel(shape_mode_frame, text="Default Shape Mode", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkOptionMenu(shape_mode_frame, values=["Sphere", "Cube", "Dots"], width=250).pack(anchor="w", padx=15, pady=(0, 15))

auto_fullscreen_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
auto_fullscreen_frame.grid(row=3, column=1, sticky="nsew", padx=10, pady=15)
CTkLabel(auto_fullscreen_frame, text="Auto Fullscreen on Start", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
CTkSwitch(auto_fullscreen_frame, text="").pack(anchor="w", padx=15, pady=(0, 15))

# Reset Button
reset_btn = CTkButton(master=settings_content, text="Reset to Default", width=180, height=35, font=("Segoe UI", 14, "bold"), fg_color="#2A2F4F", hover_color="#E5BEEC")
reset_btn.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=30)

app.mainloop()