from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("BulkKey", 0, 75, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]):
        return False
        
    if not is_any_in_array("KeyZ74", 0, 72, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]):
        return False
        
    if not is_any_in_array("Cell", 0, 72, [10, 11, 12, 13]):
        return False
        
    return True