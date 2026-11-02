# write your solution here
# Ask user for input filenames
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

# Read student names and map them by student ID
students = {}
with open(student_file, "r", encoding="utf-8") as f:
    next(f)  # Skip the header row (id;first;last)
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(";")
            student_id = parts[0]
            full_name = f"{parts[1]} {parts[2]}"
            students[student_id] = full_name

# Read exercises completed and calculate total per student ID
exercises = {}
with open(exercise_file, "r", encoding="utf-8") as f:
    next(f)  # Skip the header row (id;e1;e2;...)
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(";")
            student_id = parts[0]
            total_points = sum(int(x) for x in parts[1:])
            exercises[student_id] = total_points

# Print full name and total exercises in the order of the student file
for student_id, name in students.items():
    total = exercises.get(student_id, 0)
    print(f"{name} {total}")