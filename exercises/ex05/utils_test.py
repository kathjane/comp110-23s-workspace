"""Unit tests for only_evens, sub, concat."""

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_list1() -> None: 
    """Tests list 1 for only evens."""
    test_list: list[int] = [1, 3, 4, 6]
    assert only_evens(test_list) == [4, 6]


def test_only_evens_list2() -> None: 
    """Tests list 2 for only evens."""
    test_list: list[int] = [1, 6, 7, 89, 4]
    assert only_evens(test_list) == [6, 4]


def test_only_evens_blank_list() -> None: 
    """Test a blank list for only evens."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_sub1() -> None: 
    """Tests list 1 for correct sub."""
    test_list1: list[int] = [1, 2, 3, 4, 5]
    start_idx = 1
    end_idx = 4
    assert sub(test_list1, start_idx, end_idx) == [2, 5]


def test_sub2() -> None: 
    """Tests list 2 for correct sub."""
    test_list2: list[int] = [1, 2, 3, 4, 5]
    start_idx = 0
    end_idx = 1
    assert sub(test_list2, start_idx, end_idx) == [1, 2]


def test_sub_neg_start() -> None: 
    """Tests a list using sub with a negative start index."""
    test_list_blank: list[int] = [1, 2, 3, 4]
    start_idx = -1
    end_idx = 0
    assert sub(test_list_blank, start_idx, end_idx) == [1, 1]


def test_concat1() -> None: 
    """Tests concat of two lists."""
    test_list1: list[int] = [13, 67, 47, 86, 2]
    test_list2: list[int] = [3, 6, 7]
    assert concat(test_list1, test_list2) == [13, 67, 47, 86, 2, 3, 6, 7]


def test_concat2() -> None: 
    """Tests concat of two new lists."""
    test_list1: list[int] = [2, 4, 6, 8]
    test_list2: list[int] = [10, 12, 14]
    assert concat(test_list1, test_list2) == [13, 67, 47, 86, 2, 3, 6, 7]


def test_concat_blank() -> None: 
    """Tests concat using one blank list."""
    test_list1: list[int] = [1, 2, 3, 4]
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == [1, 2, 3, 4]
