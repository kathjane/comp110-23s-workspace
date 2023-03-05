"""EX04: Utils."""

__author__ = "730486658"


def all(input_numbers: list[int], desired_int: int) -> bool:
    """Given a list of integers it will say if they are the same as a desired int."""
    n: int = 0 
    if len(input_numbers) == 0:
        return False
    while n < len(input_numbers):
        if input_numbers[n] == desired_int:
            n = n + 1
        else: 
            return False
    return True


def max(input_list: list[int]) -> int:
    """Given a list it will return the largest integer."""
    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    # define all the variables
    input_idx: int = 0
    max_num: int = int(input_list[0])

    while input_idx < len(input_list):
        # check if current card is less than low card
        current_number: int = int(input_list[input_idx])
        if (current_number > max_num):
            # update the low card to be the value of our current card 
            max_num = current_number
        input_idx = input_idx + 1

    return max_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Check if two lists are deeply equal."""
    idx: int = 0
    if len(list_1) != len(list_2):
        return False
    while idx < len(list_1):
        if list_1[idx] == list_2[idx]:
            idx = idx + 1
        else: 
            return False
    return True