"""EX05: 'list' utility functions."""

__author__ = "730486658"


def only_evens(input_numbers: list[int]) -> list[int]:
    """Given a list of integers it will return only the even numbers."""
    idx: int = 0
    even_numbers: list[int] = list()
    while idx < len(input_numbers):
        if input_numbers[idx] % 2 == 0:
            even_numbers.append(input_numbers[idx])
            idx = idx + 1
        else: 
            idx = idx + 1
    
    return even_numbers


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists this concatanates the lists into one."""
    idx1: int = 0
    idx2: int = 0
    new_list: list[int] = list()
    while idx1 < len(list1):
        new_list.append(list1[idx1])
        idx1 = idx1 + 1
    while idx2 < len(list2):
        new_list.append(list2[idx2])
        idx2 = idx2 + 1
    return new_list


def sub(input_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Makes a new list with the start and end values pulled from the old."""
    sub_list: list[int] = list()
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(input_list) - 1:
        end_idx = len(input_list)
    if len(input_list) == 0:
        return list()
    if start_idx >= len(input_list):
        return list()
    if end_idx <= 0:
        return list()
    sub_list.append(input_list[start_idx])
    sub_list.append(input_list[end_idx - 1])

    return sub_list