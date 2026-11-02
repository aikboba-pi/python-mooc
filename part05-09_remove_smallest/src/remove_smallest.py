# Write your solution here
def remove_smallest(numbers: list):
    del numbers[numbers.index(min(numbers))]