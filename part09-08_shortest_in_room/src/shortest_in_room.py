# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self) -> bool:
        return len(self.persons) == 0

    def print_contents(self):
        total_height = sum(person.height for person in self.persons)
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None
        return min(self.persons, key=lambda person: person.height)

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person is not None:
            self.persons.remove(shortest_person)
        return shortest_person
