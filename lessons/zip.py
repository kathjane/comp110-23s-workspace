"""CQ04: Zip Function"""

def zip(list1: list[str], list2: list[int]) -> dict[str,int]:
    """Make list 1 and list 2 into a dict"""
    idx: int = 0
    output: dict[str,int] = dict()
    if len(list1) != len(list2):
        return dict()
    if len(list1) == 0: 
        return dict()
    if len(list2) == 0:
        return dict()
    while idx < len(list1):
        output[list1[idx]] = list2[idx]
        idx = idx + 1 
    
    return output

