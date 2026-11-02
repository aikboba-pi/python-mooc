# Write your solution here
res = []
current_number = 1

while True:
    print(f"The list is now {res}")

    val = input('a(d)d, (r)emove or e(x)it: ')

    if val == 'x': break
    elif val == 'd':
        res.append(current_number)
        current_number += 1
    elif val == 'r':
        current_number -= 1
        res.remove(current_number)

print('Bye!')