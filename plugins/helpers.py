
data_pulled = []


def is_any_in_array(item_name: str, item_dimension: int, item_zone: int, array: list[int]) -> bool:
    for name, dim, zone, id in data_pulled:
        if item_name == name and item_dimension == dim and item_zone == zone and id in array:
            return True
    
    return False
    

def all_in_array(item_name: str, item_dimension: int, item_zone: int, array: list[int]) -> bool:
    for name, dim, zone, id in data_pulled:
        if item_name == name and item_dimension == dim and item_zone == zone:
            if id not in array:
                return False
    
    return True


def count_in_zone(item_name: str, item_dimension: int, item_zone: int) -> int:
    count = 0
    
    for name, dim, zone, id in data_pulled:
        if name == item_name and item_dimension == dim and item_zone == zone:
            count += 1
        
    return count
    

def is_in_zone(item_name: str, item_dimension: int, item_zone: int) -> bool:
    for name, dim, zone, id in data_pulled:
        if name == item_name and item_dimension == dim and item_zone == zone:
            return True
            
    return False