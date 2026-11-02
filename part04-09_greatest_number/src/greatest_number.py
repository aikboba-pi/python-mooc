# Write your solution here
def greatest_number(num1, num2, num3):
    res = 0

    if num1 > num2:
        if num1 > num3: return num1
        else: return num3
    else:
        if num2 > num3: return num2
        else: return num3

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)