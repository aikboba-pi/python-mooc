import string

def most_common_words(filename: str, lower_limit: int) -> dict:
    with open(filename) as file:
        text = file.read()
    
    # Remove punctuation characters (like .,:;?! etc.) from each word
    words = [word.strip(string.punctuation) for word in text.split()]
    
    # Filter words appearing at least lower_limit times
    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}