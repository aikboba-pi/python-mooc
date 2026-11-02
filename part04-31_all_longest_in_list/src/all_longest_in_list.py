# Write your solution here
def all_the_longest(list: list) -> list:
    res = []
    bestLen = len(list[0])

    for item in list:
        currentLen = len(item)

        if currentLen > bestLen:
            res = [item]
            bestLen = len(item)
        elif currentLen == bestLen:
            res.append(item)
    
    return res