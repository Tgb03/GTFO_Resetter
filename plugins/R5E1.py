
from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("KeyZ529", 0, 528, [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 36, 37, 38, 39
    ]):
        return False
        
    if not is_any_in_array("KeyZ534", 0, 533, [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
        16, 17, 18, 34, 35, 36, 37, 38, 39
    ]):
        return False
        
    if not is_any_in_array("Cell", 0, 534, [0, 1, 2, 3, 4, 5, 6]):
        return False
        
    return True