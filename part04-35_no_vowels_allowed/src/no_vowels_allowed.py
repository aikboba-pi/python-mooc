# Write your solution here
def no_vowels(text: str) -> str:
    result = ""

    for char in text:
        n = ord(char) - ord("a")

        if n * (n - 4) * (n - 8) * (n - 14) * (n - 20) != 0:
            result += char

    return result