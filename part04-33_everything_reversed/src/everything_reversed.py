# Write your solution here
def everything_reversed(my_list: list) -> list:
    return list(map(lambda x: x[::-1], my_list[::-1]))