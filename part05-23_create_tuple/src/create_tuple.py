# Write your solution here
def create_tuple(x: int, y: int, z: int):
    return (min(x, y, z), max(x, y, z), x + y + z)