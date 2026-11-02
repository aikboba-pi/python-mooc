# Write your solution here
from math import factorial

def factorials(n: int) -> dict:
    return {num: factorial(num) for num in range(1, n + 1)}