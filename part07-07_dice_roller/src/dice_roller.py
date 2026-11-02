# Write your solution here
import random

def roll(die: str) -> int:
    DICE = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4],
    }

    return random.choice(DICE[die])

def play(die1: str, die2: str, times: int) -> tuple[int, int, int]:
    wins1 = 0
    wins2 = 0
    ties = 0

    for _ in range(times):
        result1 = roll(die1)
        result2 = roll(die2)

        if result1 > result2:
            wins1 += 1
        elif result2 > result1:
            wins2 += 1
        else:
            ties += 1

    return (wins1, wins2, ties)