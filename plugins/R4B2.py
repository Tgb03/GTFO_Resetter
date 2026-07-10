
from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("BulkKey", 0, 84, [0, 7, 10, 11, 12, 13]):
        return False

    if not is_any_in_array("KeyZ87", 0, 86, [0, 1, 2, 3, 4, 6, 11, 12, 13, 14, 16, 23, 24, 25, 26, 27, 28, 29, 30, 31]):
        return False
        
    #if not is_any_in_array("Cell", 0, 86, [0, 1, 2, 3, 5, 6, 7, 10, 11, 12]):
    #    return False
    #    
    if not is_any_in_array("Cell", 0, 87, [0, 1, 7, 8]):
        return False
        
    if not is_any_in_array("Cell", 0, 88, [0, 1, 4, 6, 7]):
        return False
        
    if not is_any_in_array("Cell", 0, 89, [0, 1, 2, 3, 4, 8]):
        return False
    
    return True
