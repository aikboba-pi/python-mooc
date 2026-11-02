# Write your solution here
def most_common_character(first_string: str):
    max_count = 0
    highest_char = ''

    for char in first_string:
        charCount = first_string.count(char)

        if charCount > max_count:
            max_count = charCount
            highest_char = char
    
    return highest_char