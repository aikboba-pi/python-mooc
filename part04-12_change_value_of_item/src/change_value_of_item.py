# Write your solution here
values = [1, 2, 3, 4, 5]

while True:

    index = int(input('Index: '))

    if index < 0:
        break

    value = int(input('New value: '))
    values[index] = value

    print(values)