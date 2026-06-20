
from typing import Set


data_pulled = []
marker_set = ""

# Check if any item with that name appears in the dimension, zone and one of those ids.
# 
# Use this to check if a key is within a certain list of playable keys and if not just return False
def is_any_in_array(item_name: str, item_dimension: int, item_zone: int, array: list[int]) -> bool:
    item_name = item_name.lower()
    
    for name, dim, zone, id in data_pulled:
        if item_name == name and item_dimension == dim and item_zone == zone and id in array:
            return True
    
    return False
    
# Check if all items in this dimension, zone are in the specified list
# 
# Use this to check if ALL items are within a certain list of playable ids. Use this for levels like R1B1 where you
# want all ids to be in the best room.
def all_in_array(item_name: str, item_dimension: int, item_zone: int, array: list[int]) -> bool:
    item_name = item_name.lower()
    
    for name, dim, zone, id in data_pulled:
        if item_name == name and item_dimension == dim and item_zone == zone:
            if id not in array:
                return False
    
    return True

# Check how many items appear with this name in dimension, zone and id list.
# 
# Use this if you only need like 2/3 ids to be good and you don't care about the last one. Example would be R4C2
def get_count_in_array(item_name: str, item_dimension: int, item_zone: int, array: list[int]) -> int:
    item_name = item_name.lower()
    count = 0

    for name, dim, zone, id in data_pulled:
        if item_name == name and item_dimension == dim and item_zone == zone and id in array:
            count += 1

    return count

# Count the number of items with this name in the dimension, zone
# 
# Use this when you just care about the number of items in the zone, for example R1B1 since you need 4 zones to have all 12 ids.
# Or you could check if a resource is split in 2 when you can only carry 1 tho this would be only useful for duos or solos
def count_in_zone(item_name: str, item_dimension: int, item_zone: int) -> int:
    item_name = item_name.lower()
    count = 0
    
    for name, dim, zone, id in data_pulled:
        if name == item_name and item_dimension == dim and item_zone == zone:
            count += 1
        
    return count
    
# Check if an item is in a zone
# 
# Use this when you just care about an item being in a zone but not where it is in the zone.
# Either spawns are all close or there is no timeloss as long as it is in there.
def is_in_zone(item_name: str, item_dimension: int, item_zone: int) -> bool:
    item_name = item_name.lower()
    
    for name, dim, zone, id in data_pulled:
        if name == item_name and item_dimension == dim and item_zone == zone:
            return True
            
    return False

# Checks if the hash of the level is within a set. 
# This is used mainly for levels where cells are build seed dependant like R8E2.
def is_hash_in_map(map: Set[str]) -> bool:
    return marker_set in map