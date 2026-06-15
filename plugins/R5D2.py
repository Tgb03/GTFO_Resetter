
from plugins.helpers import is_any_in_array


def check():
    return not is_any_in_array("Cell", 0, 284, [0, 1, 2, 4])
