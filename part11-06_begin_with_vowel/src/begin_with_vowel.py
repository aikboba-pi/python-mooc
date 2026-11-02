def begin_with_vowel(words: list) -> list:
    return [w for w in words if w and w[0].lower() in "aeiou"]