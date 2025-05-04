from customtkinter import *
import os
from functions import *
from HomePage import build_homepage_frame
from settings import build_settings_frame

os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = CTk()
app.geometry("600x480")

main_container = CTkFrame(app)
main_container.pack(fill="both", expand=True)

homepage_frame = CTkFrame(main_container)
homepage_frame._name = "homepage"

settings_page = CTkFrame(main_container)
settings_page._name = "settingpage"

frames = {
    "homepage": homepage_frame,
    "settingpage": settings_page
}

def show_frame(frame):
    for widget in main_container.winfo_children():
        widget.pack_forget()
    frame.pack(fill="both", expand=True)

    if hasattr(frame, "refresh"):
        frame.refresh()

build_homepage_frame(homepage_frame, show_frame, frames)
build_settings_frame(settings_page, show_frame, frames)

show_frame(homepage_frame)

app.mainloop()
