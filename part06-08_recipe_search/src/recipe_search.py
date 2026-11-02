# Write your solution here
def read_recipes(filename: str):
    recipes = []

    with open(filename, encoding="utf-8") as file:
        lines = [line.strip() for line in file]

    current_recipe = []

    # An extra empty line ensures the final recipe is processed.
    for line in lines + [""]:
        if line:
            current_recipe.append(line)
        elif current_recipe:
            name = current_recipe[0]
            preparation_time = int(current_recipe[1])
            ingredients = current_recipe[2:]

            recipes.append((name, preparation_time, ingredients))
            current_recipe = []

    return recipes


def search_by_name(filename: str, word: str):
    matches = []
    word = word.lower()

    for name, preparation_time, ingredients in read_recipes(filename):
        if word in name.lower():
            matches.append(name)

    return matches


def search_by_time(filename: str, prep_time: int):
    matches = []

    for name, preparation_time, ingredients in read_recipes(filename):
        if preparation_time <= prep_time:
            matches.append(
                f"{name}, preparation time {preparation_time} min"
            )

    return matches


def search_by_ingredient(filename: str, ingredient: str):
    matches = []
    ingredient = ingredient.lower()

    for name, preparation_time, ingredients in read_recipes(filename):
        if ingredient in [item.lower() for item in ingredients]:
            matches.append(
                f"{name}, preparation time {preparation_time} min"
            )

    return matches