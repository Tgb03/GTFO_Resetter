

from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("Cell", 0, 596, [1, 2]):
        return False
        
    if (not is_any_in_array("Cell", 0, 598, [0, 1, 2, 3, 4, 7])) and \
        (not is_any_in_array("Cell", 0, 599, [0, 1, 2, 3, 4, 11, 12])):
        return False
        
    if not is_any_in_array("Cell", 0, 602, [0, 1, 2, 11, 14, 6, 7, 8, 15, 16, 21]):
        return False
        
    return True