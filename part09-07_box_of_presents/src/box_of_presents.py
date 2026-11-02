class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self):
        self.presents = []

    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self) -> int:
        return sum(present.weight for present in self.presents)