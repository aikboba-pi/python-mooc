# Write your solution here
def filter_incorrect():
    correct_lines = []

    with open("lottery_numbers.csv", "r") as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            parts = cleaned_line.split(";")
            if len(parts) != 2:
                continue

            week_part, numbers_part = parts

            # 1. Validate week header (format: "week <integer>")
            week_split = week_part.split(" ")
            if len(week_split) != 2 or week_split[0] != "week":
                continue
            try:
                int(week_split[1])
            except ValueError:
                continue

            # 2. Split and validate the numbers
            number_strings = numbers_part.split(",")
            if len(number_strings) != 7:
                continue

            try:
                numbers = [int(num) for num in number_strings]
            except ValueError:
                # One or more elements are not integers
                continue

            # 3. Check bounds (all numbers must be between 1 and 39 inclusive)
            if any(num < 1 or num > 39 for num in numbers):
                continue

            # 4. Check for duplicates (must be 7 unique numbers)
            if len(set(numbers)) != 7:
                continue

            # If all checks pass, keep the line
            correct_lines.append(cleaned_line + "\n")

    # Write the valid lines to correct_numbers.csv
    with open("correct_numbers.csv", "w") as file:
        file.writelines(correct_lines)