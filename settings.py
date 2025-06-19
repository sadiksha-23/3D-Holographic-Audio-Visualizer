# Settings.py
from customtkinter import *
from PIL import Image
import os
from functions import *

# Set working directory to the script location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def build_settings_frame(frame, show_frame, frames):
    # Sidebar navigation frame
    sidebar_frame = CTkFrame(master=frame, fg_color="#2A2F4F", width=176, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    # App logo and title
    logo_img = CTkImage(Image.open("images/logo_icon.png"), size=(90, 90))
    CTkLabel(master=sidebar_frame, image=logo_img, text="").pack(pady=(30, 0))
    CTkLabel(master=sidebar_frame, text="3D HOLOGRAPHIC\nAUDIO VISUALIZER", font=("Segoe UI", 12, "bold"),
             text_color="white", justify="center").pack(pady=(10, 20))

    # Sidebar buttons for navigation
    CTkButton(master=sidebar_frame, image=CTkImage(Image.open("images/visualizer_icon.png"), size=(20, 20)),
          text="Visualizer", fg_color="transparent", font=("Segoe UI", 14),
          hover_color="#D9A8E3", anchor="w", compound="left",
          command=lambda: show_frame(frames["homepage"])).pack(anchor="center", ipady=5, pady=(10, 0))

    CTkButton(master=sidebar_frame, image=CTkImage(Image.open("images/settings_icon.png"), size=(20, 20)),
          text="Settings", fg_color="transparent", font=("Segoe UI", 14),
          hover_color="#D9A8E3", anchor="w", compound="left",
          command=lambda: show_frame(frames["settingpage"])).pack(anchor="center", ipady=5, pady=(16, 0))

    # Main content view
    main_view = CTkFrame(master=frame, fg_color="#917FB3", corner_radius=0)
    main_view.pack(side="left", fill="both", expand=True)
    main_view.pack_propagate(0)

    # Header section with title and profile icon
    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))
    CTkLabel(master=title_frame, text="Settings", font=("Segoe UI", 28, "bold"), text_color="#E5BEEC").pack(anchor="nw", side="left")

    profile_frame = CTkFrame(master=title_frame, fg_color="transparent")
    profile_frame.pack(anchor="ne", side="right")
    CTkLabel(master=profile_frame, image=CTkImage(Image.open("images/person_icon.png"), size=(24, 24)), text="").pack(side="left", padx=(0, 5))
    CTkLabel(master=profile_frame, text="name", font=("Segoe UI", 16), text_color="#E5BEEC").pack(side="left")

    # Content container for all setting controls
    settings_content = CTkFrame(master=main_view, fg_color="#917FB3")
    settings_content.pack(fill="both", expand=True, padx=27, pady=20)
    settings_content.grid_columnconfigure((0, 1), weight=1, uniform="a")

    # ========== ROW 1 ==========
    # Input Device Dropdown
    input_device_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
    input_device_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=15)

    def set_input_device(value):
        app_settings["input_device"] = value
        print(f"[Settings] Input Device set to: {value}")

    CTkLabel(input_device_frame, text="Input Device", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
    CTkOptionMenu(input_device_frame, values=["Default Microphone", "External Mic", "Virtual Audio Cable"], command=set_input_device, width=250).pack(anchor="w", padx=15, pady=(0, 15))

    # Color Mode Dropdown (Static or Pulse)
    color_mode_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
    color_mode_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=15)

    color_mode_var = StringVar(value=app_settings["color_mode"])
    def set_color_mode(value):
        app_settings["color_mode"] = value
        save_runtime_settings()
        print(f"Color mode set to: {value}")

    CTkLabel(color_mode_frame, text="Color Mode", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
    CTkOptionMenu(color_mode_frame, values=["Static", "Pulse"], variable=color_mode_var, command=set_color_mode, width=250).pack(anchor="w", padx=15, pady=(0, 15))

    # ========== ROW 2 ==========
    # Energy Threshold Slider
    threshold_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
    threshold_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=15)

    def set_energy_threshold(value):
        app_settings["energy_threshold"] = float(value)
        save_runtime_settings()
        print(f"Energy threshold: {value}")

    CTkLabel(threshold_frame, text="Energy Threshold", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
    energy_slider = CTkSlider(threshold_frame, from_=0, to=1, number_of_steps=100, width=250, command=set_energy_threshold)
    energy_slider.pack(anchor="w", padx=15, pady=(0, 15))
    energy_slider.set(app_settings["energy_threshold"])

    # Fullscreen Toggle Switch
    fullscreen_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
    fullscreen_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=15)

    fullscreen_switch = CTkSwitch(fullscreen_frame, text="")
    CTkLabel(fullscreen_frame, text="Auto Fullscreen on Start", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
    fullscreen_switch.pack(anchor="w", padx=15, pady=(0, 15))

    def toggle_fullscreen():
        app_settings["auto_fullscreen"] = fullscreen_switch.get()
        print(f"[Settings] Fullscreen toggle set to: {app_settings['auto_fullscreen']}")

    fullscreen_switch.configure(command=toggle_fullscreen)

    # ========== ROW 3 ==========
    # Animation Speed Slider
    speed_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
    speed_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=15)

    def set_animation_speed(value):
        app_settings["animation_speed"] = float(value)
        save_runtime_settings()
        print(f"Animation Speed set to: {value}")

    CTkLabel(speed_frame, text="Animation Speed", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
    speed_slider = CTkSlider(speed_frame, from_=0.1, to=2.0, number_of_steps=20, width=250, command=set_animation_speed)
    speed_slider.pack(anchor="w", padx=15, pady=(0, 15))

    # Detail Level Dropdown
    detail_frame = CTkFrame(settings_content, fg_color="#D79AD8", corner_radius=10)
    detail_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=15)

    detail_level_var = StringVar(value=app_settings["detail_level"])
    def set_detail_level(value):
        app_settings["detail_level"] = value
        save_runtime_settings()
        print(f"Detail level set to: {value}")

    CTkLabel(detail_frame, text="Detail Level", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(anchor="w", padx=15, pady=(15, 5))
    CTkOptionMenu(detail_frame, values=["Low", "Medium", "High"], variable=detail_level_var, command=set_detail_level, width=250).pack(anchor="w", padx=15, pady=(0, 15))

    # ========== ROW 4 ==========
    # Reset Button to restore default settings
    reset_btn = CTkButton(master=settings_content, text="Reset to Default", command=lambda: full_reset(), width=180, height=35, font=("Segoe UI", 14, "bold"), fg_color="#2A2F4F", hover_color="#E5BEEC")
    reset_btn.grid(row=3, column=0, sticky="w", padx=10, pady=(0, 15))

    # updating everything to its default state
    def full_reset():
        reset_settings()
        save_runtime_settings()
        
        # Visually update sliders and dropdowns
        color_mode_var.set(app_settings["color_mode"])
        energy_slider.set(app_settings["energy_threshold"])
        speed_slider.set(app_settings["animation_speed"])
        detail_level_var.set(app_settings["detail_level"])
        fullscreen_switch.select() if app_settings["auto_fullscreen"] else fullscreen_switch.deselect()

        print("[Settings] UI updated to reflect reset values")

