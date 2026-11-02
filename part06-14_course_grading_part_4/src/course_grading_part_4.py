# tee ratkaisu tänne
# Helper function to convert total points to course grade
def to_grade(points: int) -> int:
    if points < 15:
        return 0
    elif points < 18:
        return 1
    elif points < 21:
        return 2
    elif points < 24:
        return 3
    elif points < 28:
        return 4
    else:
        return 5

# Ask for input filenames
student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")
course_file = input("Course information: ")

# 1. Read course information
course_info = {}
with open(course_file, "r") as file:
    for line in file:
        parts = line.strip().split(":")
        if len(parts) == 2:
            course_info[parts[0].strip()] = parts[1].strip()

course_name = course_info.get("name", "")
study_credits = course_info.get("study credits", "")

# 2. Read student information (id -> full name)
students = {}
with open(student_file, "r") as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"

# 3. Read completed exercises (id -> total completed exercises count)
exercises = {}
with open(exercise_file, "r") as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = sum(int(x) for x in parts[1:])

# 4. Read exam points (id -> total exam points)
exam_points = {}
with open(exam_file, "r") as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exam_points[parts[0]] = sum(int(x) for x in parts[1:])

# Prepare data and write results.txt
header = f"{course_name}, {study_credits} credits"
divider = "=" * len(header)

txt_lines = [
    header,
    divider,
    f"{'name':30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<5}"
]

csv_lines = []

for student_id, name in students.items():
    exec_nbr = exercises.get(student_id, 0)
    # 40 exercises max: 10% gives 1 point (integer division // 4)
    exec_pts = exec_nbr // 4
    exm_pts = exam_points.get(student_id, 0)
    tot_pts = exec_pts + exm_pts
    grade = to_grade(tot_pts)

    # Line for results.txt
    txt_lines.append(
        f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<5}"
    )

    # Line for results.csv
    csv_lines.append(f"{student_id};{name};{grade}")

# Write to results.txt
with open("results.txt", "w") as file:
    file.write("\n".join(txt_lines) + "\n")

# Write to results.csv
with open("results.csv", "w") as file:
    file.write("\n".join(csv_lines) + "\n")

print("Results written to files results.txt and results.csv")