
from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("BulkKey", 0, 140, [15, 16, 17, 18, 19, 20]):
        return False

    if not is_any_in_array("GatherSmallItems", 0, 138, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]):
        return False
    
    if not is_any_in_array("GatherSmallItems", 1, 140, [1, 2, 3, 4, 5]):
        return False
        
    if not is_any_in_array("GatherSmallItems", 1, 141, [1, 3, 4, 6, 8, 9, 12, 13, 15, 16, 17, 18, 19, 20]):
        return False
    
    return True
