import unittest

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    compute_average,
)


class TestService(unittest.TestCase):
    def setUp(self):
        self.data = {
            "students": [],
            "courses": [],
            "enrollments": []
        }

    def test_add_student(self):
        student_id = add_student(self.data, "Ali")
        self.assertEqual(student_id, 1)
        self.assertEqual(len(self.data["students"]), 1)
        self.assertEqual(self.data["students"][0]["name"], "Ali")

    def test_add_grade(self):
        student_id = add_student(self.data, "Ali")
        add_course(self.data, "CS101", "Intro to CS")
        enroll(self.data, student_id, "CS101")
        add_grade(self.data, student_id, "CS101", 95)
        self.assertEqual(self.data["enrollments"][0]["grades"], [95])

    def test_compute_average(self):
        student_id = add_student(self.data, "Ali")
        add_course(self.data, "CS101", "Intro to CS")
        enroll(self.data, student_id, "CS101")
        add_grade(self.data, student_id, "CS101", 80)
        add_grade(self.data, student_id, "CS101", 100)
        average = compute_average(self.data, student_id, "CS101")
        self.assertEqual(average, 90)

    def test_add_grade_without_enrollment(self):
        student_id = add_student(self.data, "Ali")
        add_course(self.data, "CS101", "Intro to CS")

        with self.assertRaises(ValueError):
            add_grade(self.data, student_id, "CS101", 90)

    def test_duplicate_course_code_raises_error(self):
        add_course(self.data, "CS101", "Intro to CS")

        with self.assertRaises(ValueError):
            add_course(self.data, "CS101", "Another Course")

    def test_invalid_grade_raises_error(self):
        student_id = add_student(self.data, "Ali")
        add_course(self.data, "CS101", "Intro to CS")
        enroll(self.data, student_id, "CS101")

        with self.assertRaises(ValueError):
            add_grade(self.data, student_id, "CS101", 150)


if __name__ == "__main__":
    unittest.main()