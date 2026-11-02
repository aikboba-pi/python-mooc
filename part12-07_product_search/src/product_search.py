from collections.abc import Callable

def search(products: list[tuple[str, float, int]], criterion: Callable[[tuple[str, float, int]], bool]) -> list[tuple[str, float, int]]:
    return [prod for prod in products if criterion(prod)]