def filter_forbidden(string: str, forbidden: str) -> str:
    chars = [c for c in string if c not in forbidden]
    return "".join(chars)