from random import sample

def word_generator(characters: str, length: int, amount: int):
    return ("".join(sample(characters, length)) for i in range(amount))