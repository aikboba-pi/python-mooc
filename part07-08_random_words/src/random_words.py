# Write your solution here
import random


def words(n: int, beginning: str) -> list[str]:
    matching_words = []

    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()
            if word.startswith(beginning):
                matching_words.append(word)

    if len(matching_words) < n:
        raise ValueError(
            f"Not enough words starting with '{beginning}' to choose {n} unique words."
        )

    return random.sample(matching_words, n)