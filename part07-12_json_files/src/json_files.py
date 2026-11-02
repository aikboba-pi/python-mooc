# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        json_data = file.read()
    
    data = json.loads(json_data)

    for person in data:
        hobbies_str = ", ".join(person["hobbies"])
        print(f"{person['name']} {person['age']} years ({hobbies_str})")