# Write your solution here
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = {}


def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    courses = students[name]
    print(f"{name}:")
    
    if len(courses) == 0:
        print(" no completed courses")
        return

    print(f" {len(courses)} completed courses:")
    total_grades = 0
    for course_name, grade in courses.items():
        print(f"  {course_name} {grade}")
        total_grades += grade

    average_grade = total_grades / len(courses)
    print(f" average grade {average_grade}")


def add_course(students: dict, name: str, course: tuple):
    course_name, grade = course

    # Ignore courses with grade 0
    if grade == 0:
        return

    if name in students:
        # If course not yet added, or new grade is higher, record it
        if course_name not in students[name] or grade > students[name][course_name]:
            students[name][course_name] = grade


def summary(students: dict):
    print(f"students {len(students)}")

    most_courses_count = -1
    most_courses_student = ""

    best_avg_grade = -1.0
    best_avg_student = ""

    for name, courses in students.items():
        count = len(courses)
        if count > most_courses_count:
            most_courses_count = count
            most_courses_student = name

        if count > 0:
            avg_grade = sum(courses.values()) / count
            if avg_grade > best_avg_grade:
                best_avg_grade = avg_grade
                best_avg_student = name

    print(f"most courses completed {most_courses_count} {most_courses_student}")
    print(f"best average grade {best_avg_grade} {best_avg_student}")