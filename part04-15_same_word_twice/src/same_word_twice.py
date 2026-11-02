# Write your solution here
arr = []

while True:
    word = input('Word: ')

    if word in arr:
        print(f"You typed in {len(arr)} different words")
        break

    arr.append(word)