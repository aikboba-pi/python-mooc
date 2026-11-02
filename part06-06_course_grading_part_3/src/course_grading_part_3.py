# tee ratkaisu tänne
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

# Function to determine final grade
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

# Print table header
print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")

# Print each student's stats
for student_id, name in students.items():
    exec_nbr = exercises.get(student_id, 0)
    exec_pts = exec_nbr // 4
    exm_pts = exam_points.get(student_id, 0)
    tot_pts = exec_pts + exm_pts
    grade = get_grade(tot_pts)
    
    # Left-align numbers using :<10 to match left-aligned headers
    print(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}")