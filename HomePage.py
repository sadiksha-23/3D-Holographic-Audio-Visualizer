# HomePage.py
from customtkinter import *
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
import os
from functions import *

# Set working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Dummy data for the graph
revenue_data = pd.DataFrame({
    'date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'amount': np.random.randint(100, 500, 30)
})

# Globals for current mode and selected color
current_mode_var = StringVar(value=app_settings["shape_mode"])

selected_color = StringVar()
selected_color.set("#FF0000")

selected_color_name = StringVar()
selected_color_name.set("Red")

def select_color(color):
    selected_color.set(color)
    selected_color_name.set(color_names.get(color, "Unknown"))
    update_color(color)

def build_homepage_frame(frame, show_frame, frames):
    # Sidebar
    sidebar_frame = CTkFrame(master=frame, fg_color="#2A2F4F", width=176, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    logo_img = CTkImage(Image.open("logo_icon.png"), size=(90, 90))
    CTkLabel(master=sidebar_frame, image=logo_img, text="").pack(pady=(30, 0))
    CTkLabel(master=sidebar_frame, text="3D HOLOGRAPHIC\nAUDIO VISUALIZER", font=("Segoe UI", 12, "bold"),
             text_color="white", justify="center").pack(pady=(10, 20))

    CTkButton(master=sidebar_frame, image=CTkImage(Image.open("visualizer_icon.png"), size=(20, 20)),
              text="Visualizer", fg_color="transparent", font=("Segoe UI", 14),
              hover_color="#D9A8E3", anchor="w", compound="left",
              command=lambda: show_frame(frames["homepage"])).pack(anchor="center", ipady=5, pady=(10, 0))

    CTkButton(master=sidebar_frame, image=CTkImage(Image.open("settings_icon.png"), size=(20, 20)),
              text="Settings", fg_color="transparent", font=("Segoe UI", 14),
              hover_color="#D9A8E3", anchor="w", compound="left",
              command=lambda: show_frame(frames["settingpage"])).pack(anchor="center", ipady=5, pady=(16, 0))

    # Main View
    main_view = CTkFrame(master=frame, fg_color="#917FB3", corner_radius=0)
    main_view.pack(side="left", fill="both", expand=True)
    main_view.pack_propagate(0)

    # Title + Profile
    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))
    CTkLabel(master=title_frame, text="Visualizer", font=("Segoe UI", 25, "bold"), text_color="#E5BEEC").pack(anchor="nw", side="left")

    profile_frame = CTkFrame(master=title_frame, fg_color="transparent")
    profile_frame.pack(anchor="ne", side="right")
    CTkLabel(master=profile_frame, image=CTkImage(Image.open("person_icon.png"), size=(24, 24)), text="").pack(side="left", padx=(0, 5))
    CTkLabel(master=profile_frame, text="name", font=("Segoe UI", 14), text_color="#E5BEEC").pack(side="left")

    # Metric Cards
    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x", padx=27, pady=(36, 0))

    for label, value in [("Energy Level", "0.00"), ("Audio Rate", "--")]:
        card = CTkFrame(master=metrics_frame, fg_color="#D79AD8", corner_radius=10)
        card.pack(side="left", padx=5, fill="both", expand=True)
        CTkLabel(master=card, text=label, text_color="#2A2F4F", font=("Segoe UI", 14, "bold")).pack()
        CTkLabel(master=card, text=value, text_color="#2A2F4F", font=("Segoe UI", 14)).pack()

    # Mode Dropdown Card
    mode_card = CTkFrame(master=metrics_frame, fg_color="#D79AD8", corner_radius=10)
    mode_card.pack(side="left", padx=5, fill="both", expand=True)
    CTkLabel(master=mode_card, text="Mode", text_color="#2A2F4F", font=("Segoe UI", 14, "bold")).pack(pady=(5, 0))

    # Preview image container
    middle_row = CTkFrame(master=main_view, fg_color="transparent")
    middle_row.pack(fill="x", expand=False, padx=27, pady=(20, 0))

    color_picker_frame = CTkFrame(master=middle_row, fg_color="#D79AD8", width=350, height=250, corner_radius=10)
    color_picker_frame.pack_propagate(0)
    color_picker_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    CTkLabel(color_picker_frame, text="Color Palette", font=("Segoe UI", 14, "bold"), text_color="#2A2F4F").pack(pady=(10, 5))
    palette_frame = CTkFrame(master=color_picker_frame, fg_color="transparent")
    palette_frame.pack()

    for c in list(color_names.keys()):
        CTkButton(
            master=palette_frame,
            width=34,
            height=34,
            corner_radius=17,
            text="",
            fg_color=c,
            hover_color=c,
            command=lambda col=c: select_color(col)
        ).pack(side="left", padx=4, pady=10)

    CTkLabel(color_picker_frame, text="Selected Color:", font=("Segoe UI", 12, "bold"), text_color="#2A2F4F").pack(pady=(15, 0))
    CTkLabel(color_picker_frame, textvariable=selected_color_name, font=("Segoe UI", 12), text_color="#2A2F4F").pack()

    # Right image preview
    preview_image_frame = CTkFrame(master=middle_row, fg_color="#D79AD8", width=350, height=250, corner_radius=10)
    preview_image_frame.pack_propagate(0)
    preview_image_frame.pack(side="left", fill="both", expand=True, padx=(10, 0))

    CTkLabel(preview_image_frame, text="Current Mode:", font=("Segoe UI", 14, "bold"), text_color="#2A2F4F").pack(pady=(10, 0))
    CTkLabel(preview_image_frame, textvariable=current_mode_var, font=("Segoe UI", 14), text_color="#2A2F4F").pack()

    preview_label = CTkLabel(preview_image_frame, text="")
    preview_label.pack(pady=10)

    # Load default image (Cube) when page is first shown
    initial_image = CTkImage(Image.open(app_settings["preview_image_path"]), size=(220, 220))
    preview_label.configure(image=initial_image)
    preview_label.image = initial_image  # prevent garbage collection

    def update_preview_image(mode):
        update_mode(mode)                     # updates shape + preview path
        current_mode_var.set(mode)           # update label

        try:
            image = CTkImage(Image.open(app_settings["preview_image_path"]), size=(220, 220))
            preview_label.configure(image=image)
            preview_label.image = image
        except FileNotFoundError:
            print(f"⚠️ File not found: {app_settings['preview_image_path']}")


    CTkOptionMenu(
        master=mode_card,
        values=["Cube", "Sphere", "Dots"],
        variable=current_mode_var,
        command=update_preview_image,
        width=150,
        height=28,
        button_color="#2A2F4F",
        fg_color="#ffffff",
        text_color="#2A2F4F",
        dropdown_fg_color="#D79AD8",
        dropdown_hover_color="#2A2F4F",
        font=("Segoe UI", 12)
    ).pack(pady=(0, 10))

    # Graph section
    graph_frame = CTkFrame(master=main_view, fg_color="#D79AD8", corner_radius=10)
    graph_frame.pack(fill="both", expand=True, padx=27, pady=(20, 20))

    fig = Figure(figsize=(6, 2), dpi=100, facecolor="#D79AD8")
    ax = fig.add_subplot()
    ax.set_facecolor("#D79AD8")
    ax.fill_between(x=revenue_data["date"], y1=revenue_data["amount"], alpha=0.6, color="#6C63FF")
    ax.plot(revenue_data["date"], revenue_data["amount"], color="white", linewidth=2)
    ax.tick_params(labelsize=8, colors="white")
    fig.autofmt_xdate()
    ax.grid(True, linestyle="--", alpha=0.3)

    canvas = FigureCanvasTkAgg(figure=fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    def refresh_homepage_content():
        current_mode_var.set(app_settings["shape_mode"])
        try:
            image = CTkImage(Image.open(app_settings["preview_image_path"]), size=(220, 220))
            preview_label.configure(image=image)
            preview_label.image = image
        except FileNotFoundError:
            print(f"Image not found: {app_settings['preview_image_path']}")

    frame.refresh = refresh_homepage_content
