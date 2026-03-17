import csv
import os
import hashlib
import time
import statistics

class Student:
    FILE_NAME = os.path.join(os.path.dirname(__file__), "students.csv")

    def __init__(self, first_name, last_name, email_address, course_id, grades, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_id = course_id
        self.grades = grades
        self.marks = int(marks)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email_address": self.email_address,
            "course_id": self.course_id,
            "grades": self.grades,
            "marks": self.marks
        }

    @classmethod
    def load_students(c1):
        students = []

        if not os.path.exists(c1.FILE_NAME):
            return students

        with open(c1.FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = c1(
                    row["first_name"],
                    row["last_name"],
                    row["email_address"],
                    row["course_id"],
                    row["grades"],
                    row["marks"]
                )
                students.append(student)

        return students

    @classmethod
    def save_students(c1, students):
        with open(c1.FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["first_name", "last_name", "email_address", "course_id", "grades", "marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in students:
                writer.writerow(student.to_dict())

    def display_records(self):
        print("Student Record")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email_address}")
        print(f"Course ID: {self.course_id}")
        print(f"Grades: {self.grades}")
        print(f"Marks: {self.marks}")

    def add_new_student(self):

        if not self.email_address:
            print("Email cannot be empty.")
            return

        students = Student.load_students()

        for student in students:
            if student.email_address == self.email_address:
                print("Student already exists.")
                return

        students.append(self)
        Student.save_students(students)
        print("New student added successfully.")

    @classmethod
    def delete_new_student(c1, email_address):
        students = c1.load_students()
        updated_students = []

        found = False

        for student in students:
            if student.email_address == email_address:
                found = True
            else:
                updated_students.append(student)

        c1.save_students(updated_students)

        if found:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def check_my_grades(self):
        print(f"{self.first_name} {self.last_name}'s grades: {self.grades}")

    def update_student_record(self, new_first_name=None, new_last_name=None,
                              new_course_id=None, new_grades=None, new_marks=None):
        students = Student.load_students()
        found = False

        for student in students:
            if student.email_address == self.email_address:
                if new_first_name is not None:
                    student.first_name = new_first_name
                if new_last_name is not None:
                    student.last_name = new_last_name
                if new_course_id is not None:
                    student.course_id = new_course_id
                if new_grades is not None:
                    student.grades = new_grades
                if new_marks is not None:
                    student.marks = int(new_marks)

                found = True
                break

        Student.save_students(students)

        if found:
            print("Student record updated successfully.")
        else:
            print("Student not found.")

    def check_my_marks(self):
        print(f"{self.first_name} {self.last_name}'s marks: {self.marks}")
    
    @classmethod
    def sort_students_by_name(c1):
        students = c1.load_students()

        students.sort(key=lambda s: s.first_name)

        print("Students sorted by name:")

        for student in students:
            student.display_records()
            print("-" * 20)

    @classmethod
    def sort_students_by_marks(c1):
        students = c1.load_students()

        students.sort(key=lambda s: int(s.marks))

        print("Students sorted by marks:")

        for student in students:
            student.display_records()
            print("-" * 20)

    @classmethod
    def search_student(cls, email):
        import time

        students = cls.load_students()

        start_time = time.time()

        for student in students:
            if student.email_address == email:
                student.display_records()
                break

        end_time = time.time()

        print("Search time:", end_time - start_time, "seconds")
    
    @classmethod
    def calculate_average_by_course(c1, course_id):
        students = c1.load_students()

        course_marks = []

        for student in students:
            if student.course_id == course_id:
                course_marks.append(student.marks)

        if not course_marks:
            print("No records found for this course.")
            return

        average = sum(course_marks) / len(course_marks)

        print(f"Average marks for {course_id}: {average}")


    @classmethod
    def calculate_median_by_course(c1, course_id):
        students = c1.load_students()

        course_marks = []

        for student in students:
            if student.course_id == course_id:
                course_marks.append(student.marks)

        if not course_marks:
            print("No records found for this course.")
            return

        med = statistics.median(course_marks)

        print(f"Median marks for {course_id}: {med}")
    
    @classmethod
    def generate_report_by_course(cls, course_id):
        students = cls.load_students()

        print(f"Grade Report for Course: {course_id}")
        found = False

        for student in students:
            if student.course_id == course_id:
                print(f"{student.first_name} {student.last_name} | {student.grade} | {student.marks}")
                found = True

        if not found:
            print("No records found for this course.")


    @classmethod
    def generate_report_by_student(cls, email_address):
        students = cls.load_students()

        for student in students:
            if student.email_address == email_address:
                print("Grade Report for Student")
                student.display_records()
                return

        print("Student not found.")


    @classmethod
    def generate_report_by_professor(cls, professor_id):
        professors = Professor.load_professors()
        target_course_id = None

        for professor in professors:
            if professor.professor_id == professor_id:
                target_course_id = professor.course_id
                print(f"Grade Report for Professor: {professor.professor_name}")
                print(f"Course ID: {professor.course_id}")
                break

        if target_course_id is None:
            print("Professor not found.")
            return

        students = cls.load_students()
        found = False

        for student in students:
            if student.course_id == target_course_id:
                print(f"{student.first_name} {student.last_name} | {student.grade} | {student.marks}")
                found = True

        if not found:
            print("No student records found for this professor's course.")

class Course:
    FILE_NAME = os.path.join(os.path.dirname(__file__), "courses.csv")

    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "description": self.description
        }

    @classmethod
    def load_courses(cls):
        courses = []

        if not os.path.exists(cls.FILE_NAME):
            return courses

        with open(cls.FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                course = cls(
                    row["course_id"],
                    row["course_name"],
                    row["description"]
                )
                courses.append(course)

        return courses

    @classmethod
    def save_courses(cls, courses):
        with open(cls.FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["course_id", "course_name", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for course in courses:
                writer.writerow(course.to_dict())

    def display_courses(self):
        print("Course Record")
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Description: {self.description}")

    def add_new_course(self):
        if not self.course_id:
            print("Course ID cannot be empty.")
            return

        courses = Course.load_courses()

        for course in courses:
            if course.course_id == self.course_id:
                print("Course with this ID already exists.")
                return

        courses.append(self)
        Course.save_courses(courses)
        print("New course added successfully.")

    @classmethod
    def delete_new_course(cls, course_id):
        courses = cls.load_courses()
        updated_courses = []
        found = False

        for course in courses:
            if course.course_id == course_id:
                found = True
            else:
                updated_courses.append(course)

        cls.save_courses(updated_courses)

        if found:
            print("Course deleted successfully.")
        else:
            print("Course not found.")


class Professor:
    FILE_NAME = os.path.join(os.path.dirname(__file__), "professors.csv")

    def __init__(self, professor_id, professor_name, rank, course_id):
        self.professor_id = professor_id
        self.professor_name = professor_name
        self.rank = rank
        self.course_id = course_id

    def to_dict(self):
        return {
            "professor_id": self.professor_id,
            "professor_name": self.professor_name,
            "rank": self.rank,
            "course_id": self.course_id
        }

    @classmethod
    def load_professors(cls):
        professors = []

        if not os.path.exists(cls.FILE_NAME):
            return professors

        with open(cls.FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                professor = cls(
                    row["professor_id"],
                    row["professor_name"],
                    row["rank"],
                    row["course_id"]
                )
                professors.append(professor)

        return professors

    @classmethod
    def save_professors(cls, professors):
        with open(cls.FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["professor_id", "professor_name", "rank", "course_id"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for professor in professors:
                writer.writerow(professor.to_dict())

    def professors_details(self):
        print("Professor Record")
        print(f"Professor ID: {self.professor_id}")
        print(f"Professor Name: {self.professor_name}")
        print(f"Rank: {self.rank}")
        print(f"Course ID: {self.course_id}")

    def add_new_professor(self):

        if not self.professor_id:
            print("Professor ID cannot be empty.")
            return

        professors = Professor.load_professors()

        for professor in professors:
            if professor.professor_id == self.professor_id:
                print("Professor already exists.")
                return

        professors.append(self)
        Professor.save_professors(professors)
        print("New professor added successfully.")

    @classmethod
    def delete_professore(cls, professor_id):
        professors = cls.load_professors()
        updated_professors = []
        found = False

        for professor in professors:
            if professor.professor_id == professor_id:
                found = True
            else:
                updated_professors.append(professor)

        cls.save_professors(updated_professors)

        if found:
            print("Professor deleted successfully.")
        else:
            print("Professor not found.")

    def modify_professor_details(self, new_professor_name=None, new_rank=None, new_course_id=None):
        professors = Professor.load_professors()
        found = False

        for professor in professors:
            if professor.professor_id == self.professor_id:
                if new_professor_name is not None:
                    professor.professor_name = new_professor_name
                if new_rank is not None:
                    professor.rank = new_rank
                if new_course_id is not None:
                    professor.course_id = new_course_id

                found = True
                break

        Professor.save_professors(professors)

        if found:
            print("Professor record updated successfully.")
        else:
            print("Professor not found.")

    def show_course_details_by_professor(self):
        courses = Course.load_courses()

        for course in courses:
            if course.course_id == self.course_id:
                print("Course taught by this professor:")
                course.display_courses()
                return

        print("Course not found.")
        courses = Course.load_courses()

        for course in courses:
            if course.course_id == self.course_id:
                print("Course Taught By Professor")
                course.display_courses()
                return

        print("Course not found for this professor.")


class Grades:
    FILE_NAME = os.path.join(os.path.dirname(__file__), "grades.csv")

    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def to_dict(self):
        return {
            "grade_id": self.grade_id,
            "grade": self.grade,
            "marks_range": self.marks_range
        }

    @classmethod
    def load_grades(cls):
        grades = []

        if not os.path.exists(cls.FILE_NAME):
            return grades

        with open(cls.FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                grade = cls(
                    row["grade_id"],
                    row["grade"],
                    row["marks_range"]
                )
                grades.append(grade)

        return grades

    @classmethod
    def save_grades(cls, grades):
        with open(cls.FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["grade_id", "grade", "marks_range"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for grade in grades:
                writer.writerow(grade.to_dict())

    def display_grade_report(self):
        print("Grade Record")
        print(f"Grade ID: {self.grade_id}")
        print(f"Grade: {self.grade}")
        print(f"Marks Range: {self.marks_range}")

    def add_grade(self):
        grades = Grades.load_grades()

        for grade in grades:
            if grade.grade_id == self.grade_id:
                print("Grade record already exists.")
                return

        grades.append(self)
        Grades.save_grades(grades)
        print("New grade added successfully.")

    @classmethod
    def delete_grade(cls, grade_id):
        grades = cls.load_grades()
        updated_grades = []
        found = False

        for grade in grades:
            if grade.grade_id == grade_id:
                found = True
            else:
                updated_grades.append(grade)

        cls.save_grades(updated_grades)

        if found:
            print("Grade deleted successfully.")
        else:
            print("Grade not found.")

    def modify_grade(self, new_grade=None, new_marks_range=None):
        grades = Grades.load_grades()
        found = False

        for grade in grades:
            if grade.grade_id == self.grade_id:
                if new_grade is not None:
                    grade.grade = new_grade
                if new_marks_range is not None:
                    grade.marks_range = new_marks_range

                found = True
                break

        Grades.save_grades(grades)

        if found:
            print("Grade record updated successfully.")
        else:
            print("Grade not found.")


class LoginUser:
    FILE_NAME = os.path.join(os.path.dirname(__file__), "login.csv")

    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password

    def to_dict(self):
        return {
            "email_id": self.email_id,
            "password": self.password
        }

    @staticmethod
    def encrypt_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def decrypt_password():
        print("Passwords cannot be decrypted. They can only be verified.")

    @classmethod
    def load_users(cls):
        users = []

        if not os.path.exists(cls.FILE_NAME):
            return users

        with open(cls.FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                user = cls(
                    row["email_id"],
                    row["password"]
                )
                users.append(user)

        return users

    @classmethod
    def save_users(cls, users):
        with open(cls.FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["email_id", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for user in users:
                writer.writerow(user.to_dict())

    def add_user(self):
        users = LoginUser.load_users()

        for user in users:
            if user.email_id == self.email_id:
                print("User already exists.")
                return

        self.password = LoginUser.encrypt_password(self.password)
        users.append(self)
        LoginUser.save_users(users)
        print("User added successfully.")

    def login(self):
        users = LoginUser.load_users()
        encrypted_input = LoginUser.encrypt_password(self.password)

        for user in users:
            if user.email_id == self.email_id and user.password == encrypted_input:
                print("Login successful.")
                return True

        print("Invalid email or password.")
        return False

    def logout(self):
        print("Logout successful.")

    def change_password(self, new_password):
        users = LoginUser.load_users()
        found = False

        for user in users:
            if user.email_id == self.email_id:
                user.password = LoginUser.encrypt_password(new_password)
                found = True
                break

        LoginUser.save_users(users)

        if found:
            print("Password changed successfully.")
        else:
            print("User not found.")

if __name__ == "__main__":
    '''print("=== Student Test ===")
    student1 = Student("Sam", "Carpenter", "sam@mycsu.edu", "DATA200", "A", 96)
    student1.add_new_student()
    student1.display_records()
    student1.check_my_grades()
    student1.check_my_marks()

    print("\n=== Update Student Test ===")
    student1.update_student_record(new_marks=92, new_grade="A")

    print("\n=== Load All Students Test ===")
    students = Student.load_students()
    for student in students:
        student.display_records()
        print("-" * 30)

    print("\n=== Course Test ===")
    course1 = Course("DATA200", 3, "Data Science")
    course1.add_new_course()
    course1.display_courses()

    print("\n=== Professor Test ===")
    professor1 = Professor(
        "Michael Johnson",
        "michael.johnson@mycsu.edu",
        "Senior Professor",
        "DATA200"
    )
    professor1.add_new_professor()
    professor1.professors_details()
    professor1.show_course_details_by_professor()

    print("\n=== Grade Test ===")
    grade1 = Grades("G001", "A", "90-100")
    grade1.add_grade()
    grade1.display_grade_report()'''

    print("\n=== Login Test ===")
    user1 = LoginUser("michael.johnson@mycsu.edu", "Welcome123#_")
    user1.add_user()

    login_test = LoginUser("michael.johnson@mycsu.edu", "Welcome123#_")
    login_test.login()
    login_test.logout()

    '''print("\n=== Delete Student Test ===")
    Student.delete_new_student("sam@mycsu.edu")

    print("\n=== Delete Course Test ===")
    Course.delete_new_course("DATA200")

    print("\n=== Delete Professor Test ===")
    Professor.delete_professore("michael.johnson@mycsu.edu")

    print("\n=== Delete Grade Test ===")
    Grades.delete_grade("G001")'''