# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int) -> list[int]:
    numbers = random.sample(range(lower, upper + 1), amount)
    numbers.sort()
    return numbers