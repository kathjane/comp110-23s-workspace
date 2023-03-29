"""EX05: Choose Your Own Adventure."""

__author__ = "730486658"

points: int = 0
player: str = ""

def greet():
    print(f"Welcome to choose your own adventure! You are a very hungry squirrel that is preparing for winter and must collect as many nuts as you can. You will start with 0 adventure points and make choices that will determine how prepared for winter you will be.")
    print(f"Firstly, tell us your player name:")
    player = input()
    print(f"Welcome {player}, let's get started!")

def hiding_place():
    """One custom procedure"""
    print(f"Hello {player}, let's choose a place where you can hide your food for the winter")
    print(f"To choose a hiding place type 'tree', 'ground', or 'beach'")
    location: str = input()
    if location == "tree":
      print(f"Congratulations! That was the best choice, you earned 2 adventure points.")
      points =+ 2
    if location == "ground":
          print(f"That was a good choice, you earned 1 adventure point.")
          points =+ 1
    if location == "beach":
          print(f"That was not the best choice, you lost 1 adventure point.")
          points =- 1
    if location != "tree" and location != "ground" and location != "beach":
        print(f"Your answer wasn't any of the right choices, your adventure points have not changed.")

def food_collection(food_idx: int) -> int:
    "One custom function"
    """Returns a choice from the food idx that will change the number of adventure points."""
    
    food_points: int = 0
    if food_idx == 1:
        print(f"That was a good choice, you earned 1 adventure point.")
        food_points =+ 1
    if food_idx == 2:
        print(f"Congratulations! That was the best choice, you earned 2 adventure points.")
        food_points =+ 2
    if food_idx == 3:
        print(f"That was not the best choice, you lost 1 adventure point.")
        food_points =-1
    if food_idx != 1 and food_idx != 2 and food_idx != 3:
        print(f"Your answer wasn't any of the right choices, your adventure points have not changed.")
    
    print(f"Your food points are now at {food_points}")
    #points = points + food_points

if __name__ == "__main__":
    greet()
    print("What should you do first? To find a spot to hide your food type 'hide' or to collect food type 'food' or type 'done' to end the game.")
    choice: str = input()
    play: bool = True
    while play == True:
        if choice == "hide":
            hiding_place()
            print(f" You now have {points} adventure points")
            print("Choose 'hide' or 'food' again or type 'done' to exit")
            choice = input()
        if choice == "food":
            nut: str = "\U0001F330"
            apple: str = "\U0001F34E"
            lettuce: str = "\U0001F96C"
            print("Choose one of the following by typing 1, 2, or 3 based on the order they appear")
            print(f"{nut} or {apple} or {lettuce}")
            food_collection(input())
            print(f"You now have {points}")
            print("Choose 'hide' or 'food' again or type 'done' to exit")
            choice = input()
        if choice != "hide" and choice != "food" and choice != "done":
            print("I'm sorry, I didn't understnad that please try again:")
            choice = input()
        if choice == "done":
            play = False
    print(f"Congratulations, {player} you have finished preparing for winter! You ended with {points} adventure points!")
        
        
        
