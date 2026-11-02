# Copy here code of line function from previous exercise and use it in your solution
def line(length, string):
    print(('*' if len(string) == 0 else string[0]) * length)

def shape(size, character, shapeSize, shapeCharacter):
    # You should call function line here with proper parameters
    counter = 0
    
    while counter < size:
        line(counter + 1, character)
        counter += 1

    counter = 0

    while counter < shapeSize:
            line(size, shapeCharacter)
            counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")