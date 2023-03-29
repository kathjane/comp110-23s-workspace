"""EX07: Unit tests for Dictionary"""

__author__ = "730486658"

import pytest
from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

# Invert Tests
def test_invert1() -> None: 
    dict1: dict[str,str] = {"name" : "Kate", "age" : "20", "fav color" : "green"}
    result1: dict[str,str] = {"Kate" : "name", "20" : "age", "green" : "fav color"}
    assert invert(dict1) == result1 

def test_invert2() -> None: 
    dict1: dict[str,str] = {"one" : "uno", "two" : "dos", "three" : "tres"}
    result1: dict[str,str] = {"uno" : "one", "dos" : "two", "tres" : "three"}
    assert invert(dict1) == result1 

def test_invert3_edge() -> None:
    with pytest.raises(KeyError):
        my_dict = {"110" : "A", "201" : "B", "231" : "A"}
        invert(my_dict)

# Favorite Color Tests

def test_fav_color1() -> None: 
    input_dict: dict[str,str] = {"Marc" : "yellow", "Ezri" : "blue", "Kris" : "blue"}
    result: str = "blue"
    assert favorite_color(input_dict) == result

def test_fav_color2() -> None: 
    input_dict: dict[str,str] = {"Marc" : "green", "Ezri" : "green", "Kris" : "blue"}
    result: str = "green"
    assert favorite_color(input_dict) == result

def test_fav_color3_edge() -> None: 
    input_dict: dict[str,str] = {"Marc" : "green", "Ezri" : "yellow", "Kris" : "blue"}
    result: str = "green"
    assert favorite_color(input_dict) == result

# Count Tests

def test_count1() -> None:
    input_list: list[str] = ["h","a","p","p","y"]
    result: dict[str,int] = {"h" : 1, "a" : 1, "p" : 2, "y" : 1}
    assert count(input_list) == result

def test_count2() -> None:
    input_list: list[str] = ["yes","no","yes","yes","no"]
    result: dict[str,int] = {"yes" : 3, "no" : 2}
    assert count(input_list) == result

def test_count3_edge() -> None:
    input_list: list[str] = ()
    result: dict[str,int] = dict()
    assert count(input_list) == result