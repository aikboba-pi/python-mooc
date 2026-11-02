# Write your solution here
def distinct_numbers(umbers: list) -> list:
    res = []

    for num in umbers:
        if (num in res):
            continue

        res.append(num)

    return sorted(res)