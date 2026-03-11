
from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("BulkKey", 0, 459, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17]):
        return False
        
    if not is_any_in_array("KeyZ462", 0, 461, [0, 1, 2, 3, 4, 5, 21, 28, 23]):
        return False
        
    if not is_any_in_array("Cell", 0, 515, [0, 1]):
        return False
    
    if not is_any_in_array("BulkKey", 0, 516, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]):
        return False
        
    return True
