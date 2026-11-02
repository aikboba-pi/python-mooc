# Write your solution here
def older_people(people: list, year: int) -> list:
    names = []
    for name, birth_year in people:
        if birth_year < year:
            names.append(name)
    return names