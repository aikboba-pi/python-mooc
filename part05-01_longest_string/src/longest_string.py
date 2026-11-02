# Write your solution here
def longest(strings: list):
    res = ''
    resLen = 0

    for string in strings:
        if len(string) > resLen:
            res = string
            resLen = len(string)

    return res