# Write your solution here
def filter_solutions():
    correct_lines = []
    incorrect_lines = []

    with open("solutions.csv", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(";")
            name = parts[0]
            problem = parts[1]
            given_result = int(parts[2])

            # Calculate the actual result
            if "+" in problem:
                a, b = problem.split("+")
                actual_result = int(a) + int(b)
            elif "-" in problem:
                a, b = problem.split("-")
                actual_result = int(a) - int(b)

            # Compare and categorize
            if actual_result == given_result:
                correct_lines.append(line + "\n")
            else:
                incorrect_lines.append(line + "\n")

    # Write output using "w" mode to overwrite previous runs
    with open("correct.csv", "w") as file:
        file.writelines(correct_lines)

    with open("incorrect.csv", "w") as file:
        file.writelines(incorrect_lines)