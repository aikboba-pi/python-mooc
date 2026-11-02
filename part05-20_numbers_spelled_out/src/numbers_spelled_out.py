# Write your solution here
def dict_of_numbers():
    units = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }
    
    result = {}
    
    # Numbers from 0 to 19
    for i in range(20):
        result[i] = units[i]
        
    # Numbers from 20 to 99
    for i in range(20, 100):
        ten_digit = i // 10
        unit_digit = i % 10
        
        if unit_digit == 0:
            result[i] = tens[ten_digit]
        else:
            result[i] = f"{tens[ten_digit]}-{units[unit_digit]}"
            
    return result