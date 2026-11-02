# Write your solution here
from string import ascii_letters, punctuation


def separate_characters(my_string: str) -> tuple[str, str, str]:
    letters = []
    punct = []
    others = []

    for char in my_string:
        if char in ascii_letters:
            letters.append(char)
        elif char in punctuation:
            punct.append(char)
        else:
            others.append(char)

    return ("".join(letters), "".join(punct), "".join(others))