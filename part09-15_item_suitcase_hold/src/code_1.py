class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self) -> str:
        return self.__name

    def weight(self) -> int:
        return self.__weight

    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def weight(self) -> int:
        return sum(item.weight() for item in self.__items)

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        if not self.__items:
            return None
        return max(self.__items, key=lambda item: item.weight())

    def __str__(self) -> str:
        count = len(self.__items)
        item_word = "item" if count == 1 else "items"
        return f"{count} {item_word} ({self.weight()} kg)"


class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def total_weight(self) -> int:
        return sum(suitcase.weight() for suitcase in self.__suitcases)

    def add_suitcase(self, suitcase: Suitcase):
        if self.total_weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self) -> str:
        count = len(self.__suitcases)
        suitcase_word = "suitcase" if count == 1 else "suitcases"
        remaining_space = self.__max_weight - self.total_weight()
        return f"{count} {suitcase_word}, space for {remaining_space} kg"