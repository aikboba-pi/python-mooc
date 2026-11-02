# Write your solution here
def histogram(string: str):
    obj = {}

    for char in string:
        if (char not in obj):
            obj[char] = 1
            continue

        obj[char] += 1

    for char in obj:
        print(f"{char} {'*' * obj[char]}")