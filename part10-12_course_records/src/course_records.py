class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self) -> str:
        return self.__name

    def grade(self) -> int:
        return self.__grade

    def credits(self) -> int:
        return self.__credits

    def update_grade(self, grade: int):
        if grade > self.__grade:
            self.__grade = grade

    def __str__(self) -> str:
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"


class StudyRecord:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name].update_grade(grade)

    def get_course(self, name: str):
        return self.__courses.get(name, None)

    def all_courses(self) -> list:
        return list(self.__courses.values())


class StudyTrackerApplication:
    def __init__(self):
        self.__record = StudyRecord()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__record.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        course = self.__record.get_course(name)
        if course is None:
            print("no entry for this course")
        else:
            print(course)

    def statistics(self):
        courses = self.__record.all_courses()
        completed_count = len(courses)
        total_credits = sum(c.credits() for c in courses)
        
        grades = [c.grade() for c in courses]
        mean_grade = sum(grades) / completed_count if completed_count > 0 else 0.0

        print(f"{completed_count} completed courses, a total of {total_credits} credits")
        print(f"mean {mean_grade:.1f}")
        print("grade distribution")
        for g in range(5, 0, -1):
            count = grades.count(g)
            print(f"{g}: {'x' * count}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()


# When testing / submitting to the course checker:
application = StudyTrackerApplication()
application.execute()