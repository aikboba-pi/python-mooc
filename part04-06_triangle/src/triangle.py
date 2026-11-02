# Copy here code of line function from previous exercise
def line(length, string):
    print(('*' if len(string) == 0 else string[0]) * length)

def triangle(size):
    # You should call function line here with proper parameters
    counter = 0
    
    while counter < size:
        line(counter + 1, "#")
        counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
