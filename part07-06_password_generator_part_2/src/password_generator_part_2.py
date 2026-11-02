# Write your solution here
import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_special: bool) -> str:
    special_chars = "!?=+-()#"
    character_pool = string.ascii_lowercase
    password_chars = [random.choice(string.ascii_lowercase)]

    if include_numbers:
        character_pool += string.digits
        password_chars.append(random.choice(string.digits))

    if include_special:
        character_pool += special_chars
        password_chars.append(random.choice(special_chars))

    while len(password_chars) < length:
        password_chars.append(random.choice(character_pool))

    random.shuffle(password_chars)

    return "".join(password_chars)