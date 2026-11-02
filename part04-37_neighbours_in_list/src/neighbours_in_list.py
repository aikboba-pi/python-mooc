# Write your solution here
def longest_series_of_neighbours(numbers):
    if len(numbers) < 2:
        return len(numbers)
    
    longest = 1
    current = 1
    
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i-1]) == 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    
    return longest