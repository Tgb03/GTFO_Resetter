
from plugins.helpers import is_any_in_array


def check():
    if not is_any_in_array("KeyZ391", 0, 389, [0, 1, 3, 5, 6, 9, 11, 13, 15]) \
        and not is_any_in_array("KeyZ391", 0, 390, [0, 1, 2, 3, 4, 7, 9, 10, 13]):
        return False
    
    return True
