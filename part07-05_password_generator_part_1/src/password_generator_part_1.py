# Write your solution here
from string import ascii_letters
from random import choice

def generate_password(length: int):
    passwd = [choice(ascii_letters).lower() for i in range(length)]
    return "".join(passwd)