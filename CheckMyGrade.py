class Student:
    FILE_NAME = "students.csv"

    def __init__(self, first_name, last_name, email_address, course_id, grade, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

    def display_records(self):
        print("Student Record")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email_address}")
        print(f"Course ID: {self.course_id}")
        print(f"Grade: {self.grade}")
        print(f"Marks: {self.marks}")

    def add_new_student(self):
        students = Student.load_students()

        for student in students:
            if student.email_address == self.email_address:
                print("Student already exists.")
                return

        students.append(self)
        Student.save_students(students)
        print("New student added successfully.")

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
        print(f"{self.first_name} {self.last_name}'s grade: {self.grade}")

    def update_student_record(self, new_first_name=None, new_last_name=None, new_course_id=None, new_grade=None, new_marks=None):
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
                if new_grade is not None:
                    student.grade = new_grade
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


class Course:
    def __init__(self, course_id, credits, course_name):
        self.course_id = course_id
        self.credits = credits
        self.course_name = course_name

    def display_courses(self):
        pass

    def add_new_course(self):
        pass

    def delete_new_course(self):
        pass


class Professor:
    def __init__(self, name, email_address, rank, course_id):
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id

    def professors_details(self):
        pass

    def add_new_professor(self):
        pass

    def delete_professore(self):
        pass

    def modify_professor_details(self):
        pass

    def show_course_details_by_professor(self):
        pass


class Grades:
    def __init__(self, grade_id, grade, marks_range):
        self.grade_id = grade_id
        self.grade = grade
        self.marks_range = marks_range

    def display_grade_report(self):
        pass

    def add_grade(self):
        pass

    def delete_grade(self):
        pass

    def modify_grade(self):
        pass


class LoginUser:
    def __init__(self, email_id, password):
        self.email_id = email_id
        self.password = password

    def login(self):
        pass

    def logout(self):
        pass

    def change_password(self):
        pass

    def encrypt_password(self):
        pass

    def decrypt_password(self):
        pass

if __name__ == "__main__":