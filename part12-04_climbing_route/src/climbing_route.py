class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(items: list[ClimbingRoute]) -> list[ClimbingRoute]:
    return sorted(items, key=lambda item: item.length, reverse=True)

def sort_by_difficulty(items: list[ClimbingRoute]) -> list[ClimbingRoute]:
    return sorted(items, key=lambda item: (item.grade, item.length), reverse=True)