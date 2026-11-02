def sort_by_remaining_stock(items: list[tuple]) -> list[tuple]:
    return sorted(items, key=lambda item: item[2])