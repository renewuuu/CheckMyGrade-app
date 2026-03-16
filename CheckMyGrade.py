class Student:
    def __init__(self, email, first_name, last_name, course_id, grade, marks):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

    def display_record(self):

        print(
            self.email,
            self.first_name,
            self.last_name,
            self.course_id,
            self.grade,
            self.marks
        )


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for s in self.students:
            s.display_record()

if __name__ == "__main__":

    manager = StudentManager()

    s1 = Student("sam@mycsu.edu", "Sam", "Carpenter", "DATA200", "A", 96)

    manager.add_student(s1)

    manager.display_students()