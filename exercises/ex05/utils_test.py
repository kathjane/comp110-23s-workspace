"""Unit tests for only_evens, sub, concat"""

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

def test_only_evens_blank_list() -> None: 
    test_list: list[int] =[1,3,4,6]
    assert only_evens(test_list) == [4,6]

def test_sub() -> None: 
    test_list_blank: list[int] = []
    start_idx = 1
    end_idx = 4
    assert sub(test_list_blank,start_idx,end_idx) == []

def test_concat() -> None: 
    test_list1: list[int] = [13,67,47,86,2]
    test_list2: list[int] = [3,6,7]
    assert concat(test_list1, test_list2) == [13,67,47,86,2,3,6,7]
