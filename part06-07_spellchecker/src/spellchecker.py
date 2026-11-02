# write your solution here
# Read all valid words from words.txt and store them in a set for fast lookup
with open("wordlist.txt", "r", encoding="utf-8") as file:
    valid_words = {line.strip().lower() for line in file}

# Prompt user for input
text = input("Write text: ")

# Check each word and format misspelled ones with stars
result = []
for word in text.split():
    if word.lower() in valid_words:
        result.append(word)
    else:
        result.append(f"*{word}*")

# Print the reconstructed sentence
print(" ".join(result))