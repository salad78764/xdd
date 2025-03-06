import os
import requests
import ctypes
from PIL import Image
from io import BytesIO
import win32com.client


# replace this with xdd background url
BG_URL = "https://iili.io/3Fv8D11.png"
BG_PATH = os.path.join(os.getenv("TEMP"), "xddbg.png")

# Download the image and save temporarily
response = requests.get(BG_URL)
response.raise_for_status()
image = Image.open(BytesIO(response.content))
image.save(BG_PATH)
# Set wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, BG_PATH, 3)


# Change the shortcut icon 

ICON_URL = "https://iili.io/3FO4nX2.png"
ICON_PATH = os.path.join(os.getenv("TEMP"), "xddicon.ico")

# Download and save the icon image
response = requests.get(ICON_URL)
response.raise_for_status()
image = Image.open(BytesIO(response.content))
image.save(ICON_PATH, format="ICO")  # Save as .ico

desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")

shell = win32com.client.Dispatch("WScript.Shell")

# Loop through desktop files
for file in os.listdir(desktop):
    if file.endswith(".lnk"):  # Only process shortcuts
        shortcut_path = os.path.join(desktop, file)
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.IconLocation = ICON_PATH
        shortcut.Save()

