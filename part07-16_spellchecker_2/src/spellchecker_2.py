# Write your solution here
import difflib

with open('wordlist.txt') as file:
    words = [line.strip() for line in file]

word_set = set(words)
text = input('write text: ')
text_arr = text.split(' ')
result = []
wrong_items = []

for item in text_arr:
    if item.lower() in word_set:
        result.append(item)
    else:
        result.append(f"*{item}*")
        wrong_items.append(item)

print(" ".join(result))

if len(wrong_items) > 0:
    print('suggestions:')

    for wrong_item in wrong_items:
        print(f"{wrong_item}: {", ".join(difflib.get_close_matches(wrong_item.lower(), words))}")