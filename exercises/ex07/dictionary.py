"""EX07: Dictionary"""

__author__ = "730486658"

def invert(input_dict: dict[str,str]) -> dict[str,str]:
    """Given a dictionary of strings it will invert it so the keys become values and values become keys"""
    result: dict[str,str] = dict()
    value_list: list[str] = []
    key_list: list[str] = []
    
    for key in input_dict: 
        value_list.append(input_dict[key])
    
    for value in input_dict:
        key_list.append(value)
    
    idx: int = 0
    while idx < len(value_list):
        result[value_list[idx]] = key_list[idx]
        idx += 1

    # check for repeat keys
    repeat: bool = False
    list_idx1: int = 0
    list_idx2: int = 0
    while repeat == False and list_idx2 < len(value_list):
        list_idx1 = list_idx2 + 1
        while repeat == False and list_idx1 < len(value_list):
            if value_list[list_idx1] == value_list[list_idx2]:
                repeat = True
            else: 
                list_idx1 += 1
        list_idx2 += 1
    
    if repeat == True:
        raise KeyError("List cannot be inverted because keys cannot be repeated!")

    return result
    

def favorite_color(input_dict: dict[str,str]) -> str:
    """Takes a dictionary of people's favorite color and returns the color that has the most counts"""
    color_list: list[str] = []
    for key in input_dict:
        color_list.append(input_dict[key])
    
    idx = 0
    color_count: dict[str,int] = dict()
    while idx < len(color_list):
        if color_list[idx] in color_count:
            color_count[color_list[idx]] += 1
            idx += 1
        else:
            color_count[color_list[idx]] = 1
            idx += 1
    
    
    highest_v: int = 0
    for key, value in color_count.items():
        if value > highest_v:
            highest_v = value
            highest_k = key
    
    fav_color: str = highest_k

    return fav_color

def count(input_list: list[str]) -> dict[str, int]:
    result: dict[str,int] = dict()
    idx = 0

    while idx < len(input_list):
        if input_list[idx] in result:
            result[input_list[idx]] += 1
            idx += 1
        else: 
            result[input_list[idx]] = 1
            idx += 1
    
    return result
        
    