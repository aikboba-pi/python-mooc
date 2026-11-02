# Write your solution here
times = int(input('How many items: '))
counter = 1
res = []

while counter <= times:
    val = int(input(f"Item {counter}: "))
    res.append(val)
    counter += 1

print(res)