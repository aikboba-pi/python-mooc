# Write your solution here
def spruce(size):
    print('a spruce!')

    counter = 0
    char_count = 1
        
    while counter < size:
        print(f"{' ' * (size - (counter + 1))}{'*' * (char_count)}")
        
        counter += 1
        char_count += 2

    print(f"{' ' * (size - 1)}*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)