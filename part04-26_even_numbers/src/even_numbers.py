# Write your solution here
def even_numbers(arr: list):
    res = []

    for i in arr:
        if i % 2 == 0:
            res.append(i)

    return res