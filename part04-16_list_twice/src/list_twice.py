# Write your solution here
arr = []

while True:
    item = int(input('New item: '))

    if item == 0: break

    arr.append(item)

    print(f"The list now: {arr}")
    print(f"The list in order: {sorted(arr)}")

print('Bye!')