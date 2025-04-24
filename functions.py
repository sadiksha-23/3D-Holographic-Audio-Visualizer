app_settings = {
    "selected_color": "#FF0000",
    "selected_color_name": "Red",
    "current_mode": "Cube",
    "preview_image_path": "cube.png",
    "animation_speed": 1.0,
    "energy_threshold": 0.5,
    "hue_angle": 180,
    "input_device": "Default Microphone",
    "color_mode": "Static",
    "detail_level": "Medium",
    "shape_mode": "Cube",
    "auto_fullscreen": False
}

color_names = {
    "#FF0000": "Red",
    "#FF7F00": "Orange",
    "#FFFF00": "Yellow",
    "#00FF00": "Green",
    "#0000FF": "Blue",
    "#4B0082": "Indigo",
    "#8B00FF": "Violet",
    "#FFFFFF": "White",
    "#000000": "Black",
    "#808080": "Gray",
    "#FFC0CB": "Pink",
    "#00FFFF": "Cyan",
    "#FFD700": "Gold",
    "#800000": "Maroon",
    "#008080": "Teal"
}

def update_color(color):
    app_settings["selected_color"] = color
    app_settings["selected_color_name"] = color_names.get(color, "Unknown")
    print(f"Color set to {color} ({app_settings['selected_color_name']})")

def update_mode(mode):
    app_settings["shape_mode"] = mode
    app_settings["preview_image_path"] = f"{mode.lower()}.png"
    print(f"[Mode Updated] -> {mode}, Image: {app_settings['preview_image_path']}")

def apply_fullscreen(app):
    if app_settings.get("auto_fullscreen", False):
        app.after(100, lambda: app.state("zoomed"))

def reset_settings():
    app_settings.update({
        "selected_color": "#FF0000",
        "selected_color_name": "Red",
        "current_mode": "Cube",
        "preview_image_path": "cube.png",
        "animation_speed": 1.0,
        "energy_threshold": 0.5,
        "hue_angle": 180,
        "input_device": "Default Microphone",
        "color_mode": "Static",
        "detail_level": "Medium",
        "shape_mode": "Cube",
        "auto_fullscreen": False
    })
    print("[Settings] All values reset to default")



