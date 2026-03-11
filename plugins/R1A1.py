
from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("KeyZ52", 0, 50, [0, 1, 2, 3, 16, 18]):
        return False
        
    if not is_any_in_array("HSU_FindTakeSample", 0, 52, [1]):
        return False
    
    return True
