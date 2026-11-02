# Write your solution here
def read_input(text, min, max):
    while True:
        try:
            number = int(input(text))

            if (number >= min and number <= max):
                return number
        except:
            pass

        print(f"You must type in an integer between {min} and {max}")