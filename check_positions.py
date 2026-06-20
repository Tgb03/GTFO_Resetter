
# Rundown Button = 250, 25
# SelectExpedition = 700, 600
# A tier Center = 800, 275
# E tier Center = 800, 675

import sys
import json
import time
from ahk import AHK
from setup import ahk_executable_path
from get_menu_sens import menu_sensitivity

if len(sys.argv) < 2:
        print("Usage: python script.py <4-character string>")
        sys.exit(1)

level = sys.argv[1]

if len(level) != 4:
    print(f"Error: expected a 4-character string, got {len(level)} characters: '{level}'")
    sys.exit(1)

with open("resources/level_positions.json", "r", encoding="utf-8") as f:
    level_positions = json.load(f)
    level_info = level_positions.get(level, None)

ahk = AHK(version='v2', executable_path=ahk_executable_path)

pos_x_1, pos_y_1 = 250, 25
pos_x_2, pos_y_2 = level_info[0] - pos_x_1, level_info[1] - pos_y_1
pos_x_3, pos_y_3 = 700 - pos_x_2 - pos_x_1, 600 - pos_y_2 - pos_y_1

time.sleep(1)

ahk.run_script(f"""
        BlockInput("MouseMove")

        positions := [
            {{ x: -10000, y: -10000, pre: 50, click: 50 }},
            {{ x: {int(pos_x_1 / menu_sensitivity)}, y: {int(pos_y_1 / menu_sensitivity)}, pre: 50, click: 50 }},
            {{ x: {int(pos_x_2 / menu_sensitivity)}, y: {int(pos_y_2 / menu_sensitivity)}, pre: 400, click: 50 }},
        ]

        for index, pos in positions {{
            DllCall("mouse_event", "UInt", 0x0001, "Int", pos.x, "Int", pos.y, "UInt", 0, "UPtr", 0)
            Sleep(pos.pre)

            DllCall("mouse_event", "UInt", 0x0002, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0)
            Sleep(pos.click)
            DllCall("mouse_event", "UInt", 0x0004, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0)
        }}

        BlockInput("MouseMoveOff")
        """)