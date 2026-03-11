
from plugins.helpers import count_in_zone


def check():
    accessible = 0
    
    accessible += count_in_zone("GatherSmallItems", 0, 10)
    accessible += count_in_zone("GatherSmallItems", 0, 11)
    accessible += count_in_zone("GatherSmallItems", 0, 13)
    accessible += count_in_zone("GatherSmallItems", 0, 14)
        
    return accessible >= 15