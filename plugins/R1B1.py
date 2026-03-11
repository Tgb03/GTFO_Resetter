
from plugins.helpers import count_in_zone


def check():
    accessible = 0
    
    accessible += count_in_zone("GatherSmallItems", 0, 39)
    accessible += count_in_zone("GatherSmallItems", 0, 41)
    accessible += count_in_zone("GatherSmallItems", 0, 43)
    accessible += count_in_zone("GatherSmallItems", 0, 44)
        
    return accessible >= 12