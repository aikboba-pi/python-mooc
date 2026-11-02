# Write your solution here
def sum_of_positives(arr: list):
    sum = 0

    for val in arr:
        if val > 0:
            sum += val

    return sum