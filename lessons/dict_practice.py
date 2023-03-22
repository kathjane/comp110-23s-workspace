"""Practice with dictionaries"""

ice_cream: dict[str,int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 5}
ice_cream["mint"] = 3

# Adding mint
print("After adding mint: ")
print(ice_cream)

# Removing mint
ice_cream.pop("mint")
print("After removing mint: ")
print(ice_cream)

# Accessing
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# Updating a value
print("After adding one vanilla")
ice_cream["vanilla"] += 1 
print(f"Number of vanilla orders: {ice_cream['vanilla']}")
print(ice_cream)

# Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)