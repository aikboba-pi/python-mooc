# Write your solution here
def new_person(name: str, age: int) -> tuple:
    # Validate name conditions
    if not name or len(name.split()) < 2 or len(name) > 40:
        raise ValueError("Invalid name")
    
    # Validate age conditions
    if age < 0 or age > 150:
        raise ValueError("Invalid age")
        
    return (name, age)