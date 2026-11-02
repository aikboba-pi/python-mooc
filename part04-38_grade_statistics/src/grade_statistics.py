# Initialize lists to store student data
exam_points = []
exercise_points = []

# Read input until empty line
while True:
    line = input("Exam points and exercises completed: ")
    if line == "":
        break
    parts = line.split()
    exam = int(parts[0])
    exercises = int(parts[1])
    exam_points.append(exam)
    exercise_points.append(exercises // 10)  # Convert to exercise points

# Calculate total points and grades
total_points = []
grades = []

for i in range(len(exam_points)):
    total = exam_points[i] + exercise_points[i]
    total_points.append(total)
    
    # Check exam cutoff threshold first
    if exam_points[i] < 10:
        grades.append(0)
    elif total < 15:
        grades.append(0)
    elif total < 18:
        grades.append(1)
    elif total < 21:
        grades.append(2)
    elif total < 24:
        grades.append(3)
    elif total < 28:
        grades.append(4)
    else:
        grades.append(5)

# Print statistics
print("Statistics:")

# Points average
if total_points:
    avg = sum(total_points) / len(total_points)
    print(f"Points average: {avg:.1f}")
else:
    print("Points average: 0.0")

# Pass percentage (grade > 0)
if grades:
    passed = sum(1 for g in grades if g > 0)
    pass_pct = (passed / len(grades)) * 100
    print(f"Pass percentage: {pass_pct:.1f}")
else:
    print("Pass percentage: 0.0")

# Grade distribution
print("Grade distribution:")
for grade in range(5, -1, -1):
    count = grades.count(grade)
    stars = "*" * count
    print(f"  {grade}: {stars}")