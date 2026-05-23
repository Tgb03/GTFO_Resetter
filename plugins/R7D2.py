
from plugins.helpers import is_any_in_array


def check():
    return is_any_in_array("Cell", 0, 217, [1]) and is_any_in_array("ConsumableWorldspawn", 0, 209, [2, 3])