# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    return [Fraction(1, amount) for i in range(amount)]