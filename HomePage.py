# Imports necessary libraries for GUI, image handling, plotting, audio, and file operations
from customtkinter import *
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import os
from functions import *
from AudioInput import AudioInput

# Set the working directory to where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Start audio input for live energy tracking
audio_input = AudioInput()
audio_input.start()

# History list to store recent energy values for plotting
energy_history = []
max_points = 100  # Number of points to display on the energy graph

# Updates the selected color and reflects it in the GUI and persistent storage
def select_color(color):
    selected_color.set(color)
    selected_color_name.set(color_names.get(color, "Unknown"))
    update_color(color)

# Updates the preview image of the selected shape
def update_preview_image(mode):
    current_mode_var.set(mode)
    update_mode(mode)
    try:
        with open("shape.txt", "w") as f:
            f.write(mode)
        image = CTkImage(Image.open(app_settings["preview_image_path"]), size=(220, 220))
        preview_label.configure(image=image)
        preview_label.image = image
    except FileNotFoundError:
        print(f"File not found: {app_settings['preview_image_path']}")

# Main function to build the homepage GUI
def build_homepage_frame(frame, show_frame, frames):
    global current_mode_var, selected_color, selected_color_name
    
    # Tkinter variables to reflect current shape mode and color selections in the UI
    current_mode_var = StringVar(value=app_settings["shape_mode"])
    selected_color = StringVar(value=app_settings["selected_color"])
    selected_color_name = StringVar(value=app_settings["selected_color_name"])

    # Sidebar containing navigation buttons
    sidebar_frame = CTkFrame(master=frame, fg_color="#2A2F4F", width=176, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    logo_img = CTkImage(Image.open("images/logo_icon.png"), size=(90, 90))
    CTkLabel(master=sidebar_frame, image=logo_img, text="").pack(pady=(30, 0))
    CTkLabel(master=sidebar_frame, text="3D HOLOGRAPHIC\nAUDIO VISUALIZER", font=("Segoe UI", 12, "bold"),
             text_color="white", justify="center").pack(pady=(10, 20))

    # Navigation buttons for switching views
    CTkButton(master=sidebar_frame, image=CTkImage(Image.open("images/visualizer_icon.png"), size=(20, 20)),
              text="Visualizer", fg_color="transparent", font=("Segoe UI", 14), hover_color="#D9A8E3",
              anchor="w", compound="left", command=lambda: show_frame(frames["homepage"])).pack(anchor="center", ipady=5, pady=(10, 0))

    CTkButton(master=sidebar_frame, image=CTkImage(Image.open("images/settings_icon.png"), size=(20, 20)),
              text="Settings", fg_color="transparent", font=("Segoe UI", 14), hover_color="#D9A8E3",
              anchor="w", compound="left", command=lambda: show_frame(frames["settingpage"])).pack(anchor="center", ipady=5, pady=(16, 0))

    # Main view area
    main_view = CTkFrame(master=frame, fg_color="#917FB3", corner_radius=0)
    main_view.pack(side="left", fill="both", expand=True)
    main_view.pack_propagate(0)

    # Header
    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))
    CTkLabel(master=title_frame, text="Visualizer", font=("Segoe UI", 25, "bold"), text_color="#E5BEEC").pack(anchor="nw", side="left")

    # Profile icon (currently decorative)
    profile_frame = CTkFrame(master=title_frame, fg_color="transparent")
    profile_frame.pack(anchor="ne", side="right")
    CTkLabel(master=profile_frame, image=CTkImage(Image.open("images/person_icon.png"), size=(24, 24)), text="").pack(side="left")

    # Top metric cards for energy level and current mode
    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x", padx=27, pady=(36, 0))
    metrics_frame.grid_columnconfigure((0, 1), weight=1, uniform="a")

    # Energy level display
    energy_card = CTkFrame(master=metrics_frame, fg_color="#D79AD8", corner_radius=20, height=100)
    energy_card.grid(row=0, column=0, sticky="nsew", padx=5)
    CTkLabel(master=energy_card, text="Energy Level", text_color="#2A2F4F", font=("Segoe UI", 14, "bold")).pack()
    energy_label = CTkLabel(master=energy_card, text="0.00", text_color="#2A2F4F", font=("Segoe UI", 14))
    energy_label.pack()

    # Continuously updates energy label with current energy reading
    def update_energy_value():
        energy = audio_input.get_energy()
        energy_label.configure(text=f"{energy:.2f}")
        energy_label.after(100, update_energy_value)
    update_energy_value()

    # Shape mode selection dropdown
    mode_card = CTkFrame(master=metrics_frame, fg_color="#D79AD8", corner_radius=20, height=100)
    mode_card.grid(row=0, column=1, sticky="nsew", padx=5)
    CTkLabel(master=mode_card, text="Mode", text_color="#2A2F4F", font=("Segoe UI", 14, "bold")).pack(pady=(5, 0))
    CTkOptionMenu(master=mode_card, values=["Cube", "Sphere", "Dots"], variable=current_mode_var,
                  command=update_preview_image, width=150, height=28, button_color="#2A2F4F",
                  fg_color="#ffffff", text_color="#2A2F4F", dropdown_fg_color="#D79AD8",
                  dropdown_hover_color="#B98ACF", font=("Segoe UI", 12)).pack(pady=(0, 10))

    # Bottom row for color selection and preview
    bottom_row = CTkFrame(master=main_view, fg_color="transparent")
    bottom_row.pack(fill="both", expand=False, padx=27, pady=(20, 0))
    bottom_row.grid_columnconfigure((0, 1), weight=1, uniform="b")

    # Color palette selection
    color_picker_frame = CTkFrame(master=bottom_row, fg_color="#D79AD8", corner_radius=20, height=260)
    color_picker_frame.grid(row=0, column=0, sticky="nsew", padx=5)
    CTkLabel(color_picker_frame, text="Color Palette", font=("Segoe UI", 14, "bold"), text_color="#2A2F4F").pack(pady=(10, 5))
    palette_frame = CTkFrame(master=color_picker_frame, fg_color="transparent")
    palette_frame.pack()

    # Generate color buttons dynamically
    for c in list(color_names.keys()):
        CTkButton(master=palette_frame, width=34, height=34, corner_radius=17, text="", fg_color=c,
                  hover_color=c, command=lambda col=c: select_color(col)).pack(side="left", padx=4, pady=10)

    # Shows the selected color name
    CTkLabel(color_picker_frame, text="Selected Color:", font=("Segoe UI", 12, "bold"), text_color="#2A2F4F").pack(pady=(15, 0))
    CTkLabel(color_picker_frame, textvariable=selected_color_name, font=("Segoe UI", 12), text_color="#2A2F4F").pack()

    # Shape preview image
    preview_image_frame = CTkFrame(master=bottom_row, fg_color="#D79AD8", corner_radius=20, height=260)
    preview_image_frame.grid(row=0, column=1, sticky="nsew", padx=5)
    CTkLabel(preview_image_frame, text="Current Mode:", font=("Segoe UI", 14, "bold"), text_color="#2A2F4F").pack(pady=(10, 0))
    CTkLabel(preview_image_frame, textvariable=current_mode_var, font=("Segoe UI", 14), text_color="#2A2F4F").pack()
    global preview_label
    preview_label = CTkLabel(preview_image_frame, text="")
    preview_label.pack(pady=10)

    # Initialize preview image on page load
    initial_image = CTkImage(Image.open(app_settings["preview_image_path"]), size=(220, 220))
    preview_label.configure(image=initial_image)
    preview_label.image = initial_image

    # Energy graph card with matplotlib chart
    graph_frame = CTkFrame(master=main_view, fg_color="#D79AD8", corner_radius=20, height=340)
    graph_frame.pack(fill="both", expand=True, padx=27, pady=(20, 20))
    CTkLabel(master=graph_frame, text="Energy Graph", font=("Segoe UI", 16, "bold"), text_color="#2A2F4F").pack(pady=(10, 0))

    fig = Figure(figsize=(10, 2.8), dpi=100, facecolor="#D79AD8")
    ax = fig.add_subplot()
    ax.set_facecolor("#D79AD8")
    ax.grid(True, linestyle="--", alpha=0.3)
    line, = ax.plot([], [], color="white", linewidth=2)
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Recursively update the graph with new energy data
    def update_graph():
        energy = audio_input.get_energy()
        energy_history.append(energy)
        if len(energy_history) > max_points:
            energy_history.pop(0)
        line.set_data(range(len(energy_history)), energy_history)
        ax.set_xlim(0, max_points)
        ax.set_ylim(0, 1)
        canvas.draw()
        graph_frame.after(100, update_graph)

    # Refreshes UI elements like preview image when returning to homepage
    def refresh_homepage_content():
        current_mode_var.set(app_settings["shape_mode"])
        try:
            image = CTkImage(Image.open(app_settings["preview_image_path"]), size=(220, 220))
            preview_label.configure(image=image)
            preview_label.image = image
        except FileNotFoundError:
            print(f"Image not found: {app_settings['preview_image_path']}")

    # Assign the refresh function to the frame object
    frame.refresh = refresh_homepage_content

    # Start updating the graph on load
    update_graph()
