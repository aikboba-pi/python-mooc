# Write your solution here
def length_of_longest(list: list) -> str:
    best = len(list[0])

    for item in list:
        currentLen = len(item)

        if currentLen > best:
            best = currentLen
    
    return best