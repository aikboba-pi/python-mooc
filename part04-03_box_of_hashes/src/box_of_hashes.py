# Copy here code of line function from previous exercise
def line(length, string):
    print(('*' if len(string) == 0 else string[0]) * length)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    counter = height

    while counter != 0:
        line(10, "#")
        counter -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
