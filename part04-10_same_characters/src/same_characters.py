# Write your solution here
def same_chars(string, index1, index2):
    maxIndex = len(string) - 1
    
    if index1 < 0 or index1 > maxIndex or index2 < 0 or index2 > maxIndex:
        return False

    return string[index1] == string[index2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 0, 12))