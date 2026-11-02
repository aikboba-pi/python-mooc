# Write your solution here
def find_words(search_term: str) -> list:
    matches = []

    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()

            # Case 1: Search term ends with * (word must start with the prefix)
            if search_term.endswith("*"):
                prefix = search_term[:-1]
                if word.startswith(prefix):
                    matches.append(word)

            # Case 2: Search term starts with * (word must end with the suffix)
            elif search_term.startswith("*"):
                suffix = search_term[1:]
                if word.endswith(suffix):
                    matches.append(word)

            # Case 3: Search term contains dot wildcards (.) or is an exact match
            elif len(word) == len(search_term):
                match = True
                for char_search, char_word in zip(search_term, word):
                    if char_search != "." and char_search != char_word:
                        match = False
                        break
                if match:
                    matches.append(word)

    return matches