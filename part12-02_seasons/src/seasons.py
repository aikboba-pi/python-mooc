def sort_by_seasons(items: list[dict]) -> list[dict]:
    return sorted(items, key=lambda item: item["seasons"])