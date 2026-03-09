


import ctypes
import json
from operator import contains
from tkinter import *
from tkinter import ttk
import os
from ahk import AHK
import time
import json

MONITOR_SIZE_X = 2560
MONITOR_SIZE_Y = 1440

from dll_setup import CALLBACK_TYPE, lib

with open("resources/levels.json", "r", encoding="utf-8") as f:
    levels = json.load(f)

watchdog_after_id = None
watchdog_timeout = 10000  
watchdog_active = False
current_level_name = ""

def start_watchdog():
    global watchdog_after_id, watchdog_active
    cancel_watchdog()  # clear any previous
    watchdog_active = True
    watchdog_after_id = root.after(watchdog_timeout, watchdog_triggered)
    print("[WATCHDOG] Started.")

def cancel_watchdog():
    global watchdog_after_id, watchdog_active
    if watchdog_after_id is not None:
        root.after_cancel(watchdog_after_id)
        watchdog_after_id = None
    watchdog_active = False
    print("[WATCHDOG] Canceled.")

def watchdog_triggered():
    global watchdog_active
    if not watchdog_active:
        print("[WATCHDOG] Fired but inactive, ignoring.")
        return
    watchdog_active = False
    if not check_stop():
        print("[FAILSAFE] Watchdog triggered: cycle took too long, restarting...")
        cycle_reset()

ahk_executable_path = 'C:\\Program Files\\AutoHotkey\\v2\\AutoHotkey64.exe'
log_folder_path = str(os.path.join(os.getenv('USERPROFILE'), 'AppData', 'LocalLow', '10 Chambers Collective', 'GTFO'))

labels = []

root = Tk()
root.geometry("300x200")
root.title("Simple GUI for Seeds")
root.attributes('-topmost', True)

frame = ttk.Frame(root, padding=10)
frame.pack()

reset_counter = 0
reset_counter_label = Label(frame, text=f"Reset counter: {reset_counter}")
reset_counter_label.pack()

data_pulled = []
is_valid = False

ahk = AHK(version='v2', executable_path=ahk_executable_path)

@CALLBACK_TYPE
def callback_tokenizer(context, message):
    global current_level_name
    
    if message:
        data = json.loads(message)
        
        if "SelectExpedition" in data:
            rundown = data["SelectExpedition"][0]["rundown"]
            tier = data["SelectExpedition"][0]["tier"]
            level = data["SelectExpedition"][0]["level"]
            current_level_name = rundown + chr(ord("A") + tier) + chr(ord("1") + level)
            print(current_level_name)

# 4. Implement a Python callback function
# The callback returns a message that is based on the values
# u set when the callback is created by add_callback(...)
@CALLBACK_TYPE
def callback_seed_indexer(context, message):
    global reset_counter
    global reset_counter_label
    global data_pulled, is_valid

    if message:
        data = json.loads(message)
        # print(data)

        if "GenerationStart" in data:
            for label in labels:
                label.destroy()

            reset_counter += 1
            
            reset_counter_label.destroy()
            reset_counter_label = Label(frame, text=f"Reset counter: {reset_counter}")
            reset_counter_label.pack()

        if "Key" in data:
            name, dim, zone, id = data["Key"]
            text = f"{name} in ZONE_{zone} at {id}"

            if name in ["ArtifactWorldspawn", "ArtifactContainer", "ConsumableWorldspawn", "ConsumableContainer"]:
                return

            label = Label(frame, text=text)
            label.pack()
            labels.append(label)

            data_pulled.append(data["Key"])

        if data == "GenerationEnd":
            if check_stop() is False and is_valid is True:
                cycle_reset()
            else:
                cancel_watchdog()

def start_cycling():
    global is_valid
    is_valid = True
    cycle_reset()

# first pos: (0.176171875, 0.0416666667)
# second pos: varies
# third pos: (0.432421875, 0.667361111)

def cycle_reset():
    
    level_info = levels.get(current_level_name, None)
    if level_info is None:
        return
    
    start_watchdog()
    
    pos_x_1, pos_y_1 = 0.176171875, 0.0416666667
    pos_x_2, pos_y_2 = level_info["screen_position"]["x"] - pos_x_1, level_info["screen_position"]["y"] - pos_y_1
    pos_x_3, pos_y_3 = 0.25 - pos_x_2, 0.60 - pos_y_2
    
    ahk.run_script(f"""
        BlockInput("MouseMove")

        positions := [
            {{ x: -10000, y: -10000, pre: 300, click: 100, delay: 100 }},
            {{ x: {pos_x_1 * MONITOR_SIZE_X}, y: {pos_y_1 * MONITOR_SIZE_Y}, pre: 300, click: 100, delay: 100 }},
            {{ x: {pos_x_2 * MONITOR_SIZE_X}, y: {pos_y_2 * MONITOR_SIZE_Y}, pre: 300, click: 100, delay: 100 }},
            {{ x: {pos_x_3 * MONITOR_SIZE_X}, y: {pos_y_3 * MONITOR_SIZE_Y}, pre: 300, click: 900, delay: 100 }}
        ]

        for index, pos in positions {{
            DllCall("mouse_event", "UInt", 0x0001, "Int", pos.x, "Int", pos.y, "UInt", 0, "UPtr", 0)
            Sleep(pos.pre)

            DllCall("mouse_event", "UInt", 0x0002, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0)
            Sleep(pos.click)
            DllCall("mouse_event", "UInt", 0x0004, "UInt", 0, "UInt", 0, "UInt", 0, "UPtr", 0)

            Sleep(pos.delay)
        }}

        BlockInput("MouseMoveOff")
        """)


def check_stop():
    level_info = levels.get(current_level_name, None)
    if level_info is None:
        return True
    
    for name, dim, zone, id in data_pulled:
        check = level_info["lookup"].get(str(name), {}).get(str(zone), None)
        if check is not None and id not in check:
            return False
        
    return True


ahk.add_hotkey('#n', callback=start_cycling)
ahk.start_hotkeys()

# Add a callback with dummy values
callback_fn_ptr_seed_indexer = ctypes.cast(callback_seed_indexer, ctypes.c_void_p)
callback_fn_ptr_tokenizer = ctypes.cast(callback_tokenizer, ctypes.c_void_p)

lib.add_callback(4, 1, 1, 0, callback_fn_ptr_seed_indexer)
lib.add_callback(1, 1, 1, 0, callback_fn_ptr_tokenizer)

time.sleep(1)

# Start the listener thread
lib.start_listener(log_folder_path.encode('utf-8'))

root.mainloop()
