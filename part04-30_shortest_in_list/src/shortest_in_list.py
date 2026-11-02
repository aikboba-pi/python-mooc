# Write your solution here
# Write your solution here
def shortest(list: list) -> str:
    best = list[0]

    for item in list:
        currentLen = len(item)

        if currentLen < len(best):
            best = item
    
    return best