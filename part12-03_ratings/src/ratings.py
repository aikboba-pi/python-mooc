def sort_by_ratings(items: list[dict]) -> list[dict]:
    return sorted(items, key=lambda item: item["rating"], reverse = True)