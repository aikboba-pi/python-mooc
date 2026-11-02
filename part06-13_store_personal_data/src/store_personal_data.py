# Write your solution here
def store_personal_data(person: tuple):
    name, age, height = person
    line = f"{name};{age};{height}\n"
    
    with open("people.csv", "a") as file:
        file.write(line)