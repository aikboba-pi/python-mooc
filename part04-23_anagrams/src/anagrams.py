# Write your solution here
def anagrams(string1: str, string2: str):
    return ''.join(sorted(string1)) == ''.join(sorted(string2))