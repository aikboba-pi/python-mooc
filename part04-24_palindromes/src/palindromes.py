# Write your solution here
def palindromes(string: str):
    return string == string[::-1]

while True:
    some_str = input('Please type in a palindrome: ')

    if (palindromes(some_str)):
        print(f"{some_str} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
