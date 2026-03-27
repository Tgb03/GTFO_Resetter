
from typing import Set


data_pulled = []
marker_set = ""

# Check if any item with that name appears in the dimension, zone and one of those ids.
def is_any_in_array(item_name: str, item_dimension: int, item_zone: int, array: list[int]) -> bool:
    for name, dim, zone, id in data_pulled:
        if item_name == name and item_dimension == dim and item_zone == zone and id in array:
            return True
    
    return False
    
# Check if all items in this dimension, zone are in the specified list
def all_in_array(item_name: str, item_dimension: int, item_zone: int, array: list[int]) -> bool:
    for name, dim, zone, id in data_pulled:
        if item_name == name and item_dimension == dim and item_zone == zone:
            if id not in array:
                return False
    
    return True

# Count the number of items with this name in the dimension, zone
def count_in_zone(item_name: str, item_dimension: int, item_zone: int) -> int:
    count = 0
    
    for name, dim, zone, id in data_pulled:
        if name == item_name and item_dimension == dim and item_zone == zone:
            count += 1
        
    return count
    
# Check if an item is in a zone
def is_in_zone(item_name: str, item_dimension: int, item_zone: int) -> bool:
    for name, dim, zone, id in data_pulled:
        if name == item_name and item_dimension == dim and item_zone == zone:
            return True
            
    return False
    
def is_hash_in_map(map: Set[str]) -> bool:
    return marker_set in map