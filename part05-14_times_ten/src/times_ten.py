# Write your solution here
def times_ten(start_index: int, end_index: int) -> dict:
    result = {}
    for num in range(start_index, end_index + 1):
        result[num] = num * 10
    return result