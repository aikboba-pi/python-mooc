# Write your solution here
import string

def change_case(orig_string: str) -> str:
    return orig_string.swapcase()

def split_in_half(orig_string: str) -> tuple:
    mid = len(orig_string) // 2
    return orig_string[:mid], orig_string[mid:]

def remove_special_characters(orig_string: str) -> str:
    allowed_chars = string.ascii_letters + string.digits + " "
    return "".join(char for char in orig_string if char in allowed_chars)