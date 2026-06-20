from plugins.helpers import is_any_in_array, is_hash_in_map

def check():
    if not is_any_in_array("Ammopack", 0, 491, [
        2, 9, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 25, 27
    ]):
        return False
        
    if not is_any_in_array("Ammopack", 0, 492, [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
    ]):
        return False
        
    if not is_any_in_array("Ammopack", 0, 493, [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 47, 48, 49, 50, 51, 52
    ]):
        return False
    
    if not is_any_in_array("BulkKey", 0, 495, [
        0, 1, 2, 3, 4, 5, 12, 13, 14, 15
    ]):
        return False
        
    return is_hash_in_map({
        "72f6e992bdc2367bc09726ac666d03b0c0b0e342fae4db119a8ac236fa7c238f", # one cell A
        "8322efb80909976ee345620803d8a1f3a38ad53a89eab8c7b320bb167db9d5ff", # both cell A
        "47d81649207b0f14dbadf2210942e368b1b33ce1a99fb468e52af70f18fa988b"  # goofy front cell A
    })