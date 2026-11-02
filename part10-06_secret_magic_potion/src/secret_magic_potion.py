class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self._password = password

    def _check_password(self, password: str):
        if password != self._password:
            raise ValueError("Wrong password!")

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        self._check_password(password)
        super().add_ingredient(ingredient, amount)

    def print_recipe(self, password: str):
        self._check_password(password)
        super().print_recipe()