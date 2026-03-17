import unittest
import time
from CheckMyGrade import Student, Course, Professor


class TestCheckMyGrade(unittest.TestCase):

    def test_student_records(self):
        students = Student.load_students()
        self.assertGreaterEqual(len(students), 1000)

    def test_add_student(self):
        student = Student(
            "Test",
            "User",
            "testuser@mycsu.edu",
            "DATA200",
            "A",
            95
        )

        student.add_new_student()
        students = Student.load_students()

        found = any(s.email_address == "testuser@mycsu.edu" for s in students)
        self.assertTrue(found)

    def test_update_student(self):
        student = Student(
            "Update",
            "User",
            "updateuser@mycsu.edu",
            "DATA200",
            "B",
            80
        )
        student.add_new_student()
        student.update_student_record(new_marks=88, new_grades="B")

        students = Student.load_students()
        updated_student = None

        for s in students:
            if s.email_address == "updateuser@mycsu.edu":
                updated_student = s
                break

        self.assertIsNotNone(updated_student)
        self.assertEqual(updated_student.marks, 88)

    def test_delete_student(self):
        student = Student(
            "Delete",
            "User",
            "deleteuser@mycsu.edu",
            "DATA200",
            "C",
            70
        )
        student.add_new_student()
        Student.delete_new_student("deleteuser@mycsu.edu")

        students = Student.load_students()
        found = any(s.email_address == "deleteuser@mycsu.edu" for s in students)
        self.assertFalse(found)

    def test_search_student_with_time(self):
        start = time.time()
        students = Student.load_students()

        found = False
        for s in students:
            if s.email_address == "student0100@mycsu.edu":
                found = True
                break

        end = time.time()
        print("Search time:", end - start)

        self.assertTrue(found)

    def test_sort_students_by_marks_with_time(self):
        students = Student.load_students()

        start = time.time()
        students.sort(key=lambda s: s.marks)
        end = time.time()

        print("Sort time by marks:", end - start)

        self.assertLessEqual(students[0].marks, students[-1].marks)

    def test_sort_students_by_email_with_time(self):
        students = Student.load_students()

        start = time.time()
        students.sort(key=lambda s: s.email_address.lower())
        end = time.time()

        print("Sort time by email:", end - start)

        self.assertLessEqual(
            students[0].email_address.lower(),
            students[-1].email_address.lower()
        )

    def test_add_course(self):
        course = Course("TEST101", "Test Course", "Test Description")
        course.add_new_course()

        courses = Course.load_courses()
        found = any(c.course_id == "TEST101" for c in courses)
        self.assertTrue(found)

    def test_delete_course(self):
        course = Course("DEL101", "Delete Course", "Delete Description")
        course.add_new_course()
        Course.delete_new_course("DEL101")

        courses = Course.load_courses()
        found = any(c.course_id == "DEL101" for c in courses)
        self.assertFalse(found)

    def test_modify_course(self):
        course = Course("MOD101", "Old Course", "Old Description")
        course.add_new_course()

        courses = Course.load_courses()
        for c in courses:
            if c.course_id == "MOD101":
                c.course_name = "New Course"
                c.description = "New Description"

        Course.save_courses(courses)

        courses = Course.load_courses()
        modified = None
        for c in courses:
            if c.course_id == "MOD101":
                modified = c
                break

        self.assertIsNotNone(modified)
        self.assertEqual(modified.course_name, "New Course")

    def test_add_professor(self):
        professor = Professor(
            "test.prof@mycsu.edu",
            "Test Professor",
            "Assistant Professor",
            "DATA200"
        )
        professor.add_new_professor()

        professors = Professor.load_professors()
        found = any(p.professor_id == "test.prof@mycsu.edu" for p in professors)
        self.assertTrue(found)

    def test_delete_professor(self):
        professor = Professor(
            "delete.prof@mycsu.edu",
            "Delete Professor",
            "Assistant Professor",
            "DATA200"
        )
        professor.add_new_professor()
        Professor.delete_professore("delete.prof@mycsu.edu")

        professors = Professor.load_professors()
        found = any(p.professor_id == "delete.prof@mycsu.edu" for p in professors)
        self.assertFalse(found)

    def test_modify_professor(self):
        professor = Professor(
            "modify.prof@mycsu.edu",
            "Old Professor",
            "Assistant Professor",
            "DATA200"
        )
        professor.add_new_professor()
        professor.modify_professor_details(
            new_professor_name="New Professor",
            new_rank="Senior Professor"
        )

        professors = Professor.load_professors()
        modified = None

        for p in professors:
            if p.professor_id == "modify.prof@mycsu.edu":
                modified = p
                break

        self.assertIsNotNone(modified)
        self.assertEqual(modified.professor_name, "New Professor")


if __name__ == "__main__":
    unittest.main()