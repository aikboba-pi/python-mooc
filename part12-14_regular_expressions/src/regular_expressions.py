# Write your solution here
from re import search

def is_dotw(my_string: str) -> bool:
    if (search("^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$", my_string)):
        return True
    else:
        return False

def all_vowels(my_string: str) -> bool:
    if search("^[aeiouAEIOU]+$", my_string):
        return True
    else:
        return False

def time_of_day(my_string: str) -> bool:
    if search("^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    else:
        return False