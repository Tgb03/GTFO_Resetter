
import json

from setup import log_folder_path


with open(log_folder_path + "/GTFO_Settings.txt", "r", encoding="utf-8") as f:
    menu_sensitivity = json.load(f)["Gameplay"]["LookSpeedMenu"]["Value"]
    
