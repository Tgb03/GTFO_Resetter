
from ctypes import c_char_p, c_void_p, c_uint8, c_uint32, CFUNCTYPE
import ctypes
from pathlib import Path
import os

dll_relative_path = "resources\\glr_dylib.dll"

#
# THIS IS ALL SETUP FOR THE DLL
# You could throw all this in a python class
# This will remain static.
#

# Get absolute path to the DLL relative to this script
script_dir = Path(__file__).resolve().parent
dll_path = os.path.join(script_dir, dll_relative_path)
  # Replace with actual DLL name
lib = ctypes.CDLL(dll_path)

# 2. Define callback type: extern "C" fn(context: *const c_void, message: *const c_char)
CALLBACK_TYPE = CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_char_p)

# 3. Define Rust function signatures

# void start_listener(const char* file_path)
lib.start_listener.argtypes = [c_char_p]
lib.start_listener.restype = None

# void add_callback(uint8_t code, uint8_t message_type, uint32_t channel_id, void* context, void* callback)
lib.add_callback.argtypes = [c_uint8, c_uint8, c_uint32, c_void_p, c_void_p]
lib.add_callback.restype = None

# void remove_callback(uint32_t channel_id)
lib.remove_callback.argtypes = [c_uint8, c_uint32]
lib.remove_callback.restype = None

#
# THIS IS WHERE THE ACTUAL CODE STARTS
# From here u can modify the code and do whatever u want with it.
#
