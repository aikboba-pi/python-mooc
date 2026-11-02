# Write your solution here
def invert(dictionary: dict):
    # Store inverted key-value pairs temporarily
    inverted = {value: key for key, value in dictionary.items()}
    
    # Clear the original dictionary and update it with the inverted pairs
    dictionary.clear()
    dictionary.update(inverted)