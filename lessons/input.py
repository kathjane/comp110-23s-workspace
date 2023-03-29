"""Demonstrates asking the user for input"""

# user_name: str = input("What is your name? ")
# print("Hello, " + user_name + ", good morning!")
# print("You are the best programmer ever, " + user_name)

#x: int = 1

#def f(y: int) -> int:
  #return x + y

#print(f(x + 1))

food_idx: int = 3
nut: str = "\U0001F330"
apple: str = "\U0001F34E"
lettuce: str = "\U0001F96C"
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
        

