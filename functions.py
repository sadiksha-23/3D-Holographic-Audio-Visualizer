import os

# Define base paths for saving settings and resources (shape/color)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SHAPE_PATH = os.path.join(BASE_DIR, "shape.txt")
SETTINGS_STATE_PATH = os.path.join(BASE_DIR, "state_settings.txt")
COLOR_PATH = os.path.join(BASE_DIR, "color.txt")

# Application-wide configuration dictionary
app_settings = {
    "selected_color": "#FF0000",              # Default visual color
    "selected_color_name": "Red",             # Name of the default color
    "current_mode": "Cube",                   # Initial mode
    "preview_image_path": "images/cube.png",  # Preview image shown in GUI
    "animation_speed": 1.0,                   # Default animation speed
    "energy_threshold": 0,                    # Minimum energy needed to trigger visuals
    "input_device": "Default Microphone",     # Audio input source
    "color_mode": "Static",                   # Color behavior: Static or Pulse
    "shape_mode": "Cube",                     # Default visual shape
    "detail_level": "Medium",                 # Visual detail: Low, Medium, High
    "auto_fullscreen": False                  # Whether to launch visualizer in fullscreen
}

# Map shape names to mode numbers
shape_map = {
    "Cube": 1,
    "Sphere": 2,
    "Dots": 3
}

# Color HEX to readable name mapping
color_names = {
    "#FF0000": "Red",          
    "#FF7F00": "Orange",       
    "#FFFF00": "Yellow",       
    "#00FF00": "Neon Green",   
    "#0000FF": "Electric Blue",
    "#FF00FF": "Magenta",      
    "#00FFFF": "Cyan",         
    "#40E0D0": "Turquoise",   
    "#FFA500": "Bright Orange",
    "#00FF7F": "Spring Green", 
    "#8A2BE2": "Blue Violet",  
    "#FF1493": "Deep Pink",    
}

# Save new color to memory and file
def update_color(color):
    app_settings["selected_color"] = color
    app_settings["selected_color_name"] = color_names.get(color, "Unknown")
    with open(COLOR_PATH, "w") as f:
        f.write(color)

# Save new mode to memory and shape file
def update_mode(mode):
    app_settings["shape_mode"] = mode
    app_settings["preview_image_path"] = f"images/{mode.lower()}.png"
    try:
        with open(SHAPE_PATH, "w") as f:
            f.write(mode)
    except Exception as e:
        print("Failed to write shape.txt:", e)
    print(f"[Mode Updated] -> {mode}, Image: {app_settings['preview_image_path']}")

# Apply fullscreen behavior if setting is enabled
def apply_fullscreen(app):
    if app_settings.get("auto_fullscreen", False):
        app.after(100, lambda: app.state("zoomed"))

# Reset all settings to defaults
def reset_settings():
    app_settings.update({
        "selected_color": "#FF0000",
        "selected_color_name": "Red",
        "current_mode": "Cube",
        "preview_image_path": "images/cube.png",
        "animation_speed": 1.0,
        "energy_threshold": 0,
        "input_device": "Default Microphone",
        "color_mode": "Static",
        "shape_mode": "Cube",
        "detail_level": "Medium",
        "auto_fullscreen": False
    })
    print("[Settings] All values reset to default")

# User login validation using users.txt file
def authenticate_user(email, password):
    try:
        with open(os.path.join(BASE_DIR, "users.txt"), "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue  # skip malformed lines
                saved_email, saved_password = parts
                if saved_email == email and saved_password == password:
                    return True
    except FileNotFoundError:
        return False
    return False


# Convert HEX color code to RGB tuple
def hex_to_rgb(hex_color):
    hex_color = hex_color.strip().lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Load shape mode from shape.txt or fallback to default
def get_saved_shape():
    try:
        with open(SHAPE_PATH, "r") as f:
            shape = f.read().strip()
            if shape in shape_map:
                return shape
    except:
        pass
    default_shape = app_settings["shape_mode"]
    with open(SHAPE_PATH, "w") as f:
        f.write(default_shape)
    return default_shape

# Load color from color.txt or fallback to default
def get_saved_color():
    try:
        with open(COLOR_PATH, "r") as f:
            color = f.read().strip()
            if color.startswith("#") and len(color) == 7:
                return color
    except:
        pass
    default_color = app_settings["selected_color"]
    with open(COLOR_PATH, "w") as f:
        f.write(default_color)
    return default_color

# Adjust color brightness dynamically based on audio energy
def apply_pulse_color(base_color, energy):
    boosted = 0 if energy < app_settings["energy_threshold"] else min(energy * 10, 1.0)
    factor = 0.5 + 0.5 * boosted
    return tuple(min(int(c * factor), 255) for c in base_color)

# Save persistent state settings in a single line (used for recovery/reload)
def save_state_settings():
    with open(SETTINGS_STATE_PATH, "w") as f:
        f.write(f"{app_settings['energy_threshold']},{app_settings['animation_speed']},{app_settings['color_mode']},{app_settings['detail_level']}")

# Save settings in a multiline format (used for live update)
def save_runtime_settings():
    with open("state_settings.txt", "w") as f:
        f.write(f"{app_settings['animation_speed']}\n")
        f.write(f"{app_settings['energy_threshold']}\n")
        f.write(f"{app_settings['color_mode']}\n")
        f.write(f"{app_settings['detail_level']}\n")




