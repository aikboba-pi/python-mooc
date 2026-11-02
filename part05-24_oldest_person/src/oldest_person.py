# Write your solution here
def oldest_person(people: list) -> str:
    # The oldest person has the smallest birth year
    oldest = people[0]
    
    for person in people[1:]:
        if person[1] < oldest[1]:
            oldest = person
            
    return oldest[0]