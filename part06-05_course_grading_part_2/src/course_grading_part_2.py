# write your solution here
# Prompt for input filenames
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

# Read student names mapped by student ID
students = {}
with open(student_file, "r", encoding="utf-8") as f:
    next(f)  # Skip header
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(";")
            student_id = parts[0]
            students[student_id] = f"{parts[1]} {parts[2]}"

# Read and sum completed exercises per student ID
exercises = {}
with open(exercise_file, "r", encoding="utf-8") as f:
    next(f)  # Skip header
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(";")
            student_id = parts[0]
            exercises[student_id] = sum(int(x) for x in parts[1:])

# Read and sum exam points per student ID
exam_points = {}
with open(exam_file, "r", encoding="utf-8") as f:
    next(f)  # Skip header
    for line in f:
        line = line.strip()
        if line:
            parts = line.split(";")
            student_id = parts[0]
            exam_points[student_id] = sum(int(x) for x in parts[1:])

# Calculate grade based on total points (exam points + exercise points)
def get_grade(total_points):
    if total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

# Print each student's name and their final grade
for student_id, name in students.items():
    total_exercises = exercises.get(student_id, 0)
    # 40 total exercises -> 10% is 4 exercises per 1 exercise point (integer division)
    exercise_pts = total_exercises // 4
    exam_pts = exam_points.get(student_id, 0)
    
    total_pts = exam_pts + exercise_pts
    grade = get_grade(total_pts)
    
    print(f"{name} {grade}")