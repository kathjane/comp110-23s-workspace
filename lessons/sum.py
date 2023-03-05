"""Example function for unit tests."""

def old_sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs): 
        sum_total += xs[idx]
        idx += 1
    return sum_total


def sum_with_for(xs: list[float]) -> float:
    """return sum of all the elements using a for loop"""
    sum_total: int = 0
    for numbers in xs:
        sum_total += numbers
    return sum_total

def sum(xs: list[float]) -> float:
    """return sum of all the elements using a for in range loop"""
    sum_total: float = 0 
    for number in range(0, len(xs)):
        sum_total += xs[number]
    return sum_total

print(sum([1,2,3,4]))