# write your solution here
def largest():
    with open("numbers.txt") as my_file:
        return int(max(my_file, key=lambda i: int(i)))