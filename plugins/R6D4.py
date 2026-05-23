
from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("KeyZ412", 0, 410, [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]):
        return False

    if not is_any_in_array("Cell", 0, 414, [0, 1, 2, 3, 4, 5]):
        return False
        
    if not is_any_in_array("GatherSmallItems", 0, 416, [0, 1, 3, 6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19, 20]):
        return False
        
    if not is_any_in_array("GatherSmallItems", 1, 413, [0, 2, 3, 6, 7]):
        return False

    if not is_any_in_array("KeyZ414", 2, 413, [0, 2, 3, 6, 7]):
        return False
        
    if not is_any_in_array("KeyZ411", 3, 412, [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]):
        return False
        
    if not is_any_in_array("GatherSmallItems", 3, 411, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 19]):
        return False
        
    if not is_any_in_array("Cell", 0, 414, [0, 1, 2, 3, 4]):
        return False
        
    return False
