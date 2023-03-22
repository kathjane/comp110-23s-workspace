"""EX05: Choose Your Own Adventure."""

__author__ = "730486658"

points: int = 0
player: str = input()

def greet():
    print(f"Welcome to choose your own adventure! You are a very hungry squirrel that is preparing for winter and must collect as many nuts as you can. You will start with 0 adventure points and make choices that will determine how prepared for winter you will be.")
    print(f"Firstly, tell us your player name: {player}")
    print(f"Welcome {player}, let's get started!")

def hiding_place():
    print(f"Hello {player}, let's choose a place where you can hide your food for the winter")
    location: str = input()
    print(f"To choose a hiding place type 'tree', 'ground', or 'beach' {location}")
    if location == "tree":
        print(f"Congratulations! That was the best choice, you earned 2 adventure points.")
        points =+ 2
    if location == "ground":
        print(f"That was a good choice, you earned 1 adventure point.")
        points =+ 1
    if location == "beach":
        print(f"That was not the best choice, you lost 1 adventure point.")
        points =- 1
    if location != "tree" or "ground" or "beach":
        print(f"Your answer wasn't any of the right choices, please try again: ")
        location = input()

def food_collection(food_idx: int) -> int:
    """Returns a choice from the food idx that will change the number of adventure points."""
