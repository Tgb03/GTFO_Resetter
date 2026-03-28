


import ctypes
import json
from tkinter import Label, Tk, ttk
import os
from ahk import AHK
import time
import json

from script_loader import load_plugins, plugins
from setup import ahk_executable_path, log_folder_path
from dll_setup import CALLBACK_TYPE, lib
from get_menu_sens import menu_sensitivity
from plugins.helpers import data_pulled, marker_set

with open("resources/level_positions.json", "r", encoding="utf-8") as f:
    level_positions = json.load(f)

watchdog_after_id = None
watchdog_timeout = 10000  
watchdog_active = False
current_level_name = ""

load_plugins()

def start_watchdog():
    global watchdog_after_id, watchdog_active
    cancel_watchdog()  # clear any previous
    watchdog_active = True
    watchdog_after_id = root.after(watchdog_timeout, watchdog_triggered)

def cancel_watchdog():
    global watchdog_after_id, watchdog_active
    if watchdog_after_id is not None:
        root.after_cancel(watchdog_after_id)
        watchdog_after_id = None
    watchdog_active = False

def watchdog_triggered():
    global watchdog_active
    if not watchdog_active:
        return
    watchdog_active = False
    if not check_stop():
        cycle_reset()

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
    global data_pulled, marker_set, is_valid

    if message:
        data = json.loads(message)
        # print(data)

        if "GenerationStart" in data:
            for label in labels:
                label.destroy()

            data_pulled.clear()
            marker_set = ""
            reset_counter += 1
            
            reset_counter_label.destroy()
            reset_counter_label = Label(frame, text=f"Reset counter: {reset_counter}")
            reset_counter_label.pack()

        if "Key" in data:
            name, dim, zone, id = data["Key"]
            text = f"{name} in ZONE_{zone} at {id}"
            name = name.lower()
            data_pulled.append(data["Key"])

            if name in ["artifactworldspawn", "artifactcontainer", "consumableworldspawn", "consumablecontainer"]:
                return

            label = Label(frame, text=text)
            label.pack()
            labels.append(label)
            
        if "ResourcePack" in data:
            name, dim, zone, id, size = data["ResourcePack"]
            name = name.lower()
            data_pulled.append([name, dim, zone, id])
            
        if "GenerationOverflowHash" in data:
            b = bytes(data["GenerationOverflowHash"])
            marker_set = b.hex()

        if data == "GenerationEnd":
            if check_stop() is False and is_valid is True:
                cycle_reset()
            else:
                cancel_watchdog()

def start_cycling():
    global is_valid
    is_valid = True
    cycle_reset()

# Rundown Button = 250, 25
# SelectExpedition = 700, 600
# A tier Center = 800, 275
# E tier Center = 800, 675

pos_x_1, pos_y_1 = 250, 25

def cycle_reset():
    
    level_info = level_positions.get(current_level_name, None)
    if level_info is None:
        print("Exit because level_info was none")
        return
    
    start_watchdog()
    
    pos_x_2, pos_y_2 = level_info[0] - pos_x_1, level_info[1] - pos_y_1
    pos_x_3, pos_y_3 = 700 - pos_x_2 - pos_x_1, 600 - pos_y_2 - pos_y_1
    
    ahk.run_script(f"""
        BlockInput("MouseMove")

        positions := [
            {{ x: -10000, y: -10000, pre: 50, click: 50 }},
            {{ x: {int(pos_x_1 / menu_sensitivity)}, y: {int(pos_y_1 / menu_sensitivity)}, pre: 50, click: 50 }},
            {{ x: {int(pos_x_2 / menu_sensitivity)}, y: {int(pos_y_2 / menu_sensitivity)}, pre: 400, click: 50 }},
            {{ x: {int(pos_x_3 / menu_sensitivity)}, y: {int(pos_y_3 / menu_sensitivity)}, pre: 100, click: 900 }}
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


def check_stop():
    func = plugins.get(current_level_name)
    
    if func is None:
        print("Exit because func was none")
        return True

    return func()

# Start the listener thread
lib.start_listener(log_folder_path.encode('utf-8'))
time.sleep(1)

ahk.add_hotkey('#n', callback=start_cycling)
ahk.start_hotkeys()

# Add a callback with dummy values
callback_fn_ptr_seed_indexer = ctypes.cast(callback_seed_indexer, ctypes.c_void_p)
callback_fn_ptr_tokenizer = ctypes.cast(callback_tokenizer, ctypes.c_void_p)

lib.add_callback(4, 1, 1, 0, callback_fn_ptr_seed_indexer)
lib.add_callback(1, 1, 1, 0, callback_fn_ptr_tokenizer)

root.mainloop()
