# Write your solution here
def list_sum(list1: list, list2: list) -> list:
    res = []

    for i in range(len(list1)):
        res.append(list1[i] + list2[i])
    
    return res