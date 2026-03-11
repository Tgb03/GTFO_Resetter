
from plugins.helpers import all_in_array, is_any_in_array


def check():
    if not (is_any_in_array("Cell", 0, 213, [7]) or 
        is_any_in_array("Cell", 0, 214, [0, 1])):
        return False
    
    if not all_in_array("Cell", 0, 217, [0, 1, 2, 11, 12]):
        return False
    
    if not is_any_in_array("Cell", 0, 218, [0, 1, 2, 6]):
        return False
        
    return True