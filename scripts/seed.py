import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from gradebook.storage import save_data
from gradebook.service import add_student, add_course, enroll, add_grade


def main():
    """Create sample gradebook data and save it to the JSON file."""
    data = {
        "students": [],
        "courses": [],
        "enrollments": []
    }

    student_1 = add_student(data, "Ali Veli")
    student_2 = add_student(data, "Ayse Yilmaz")
    student_3 = add_student(data, "Mehmet Demir")

    add_course(data, "CS101", "Intro to CS")
    add_course(data, "MATH101", "Calculus I")

    enroll(data, student_1, "CS101")
    enroll(data, student_1, "MATH101")
    enroll(data, student_2, "CS101")
    enroll(data, student_3, "MATH101")

    add_grade(data, student_1, "CS101", 90)
    add_grade(data, student_1, "CS101", 80)
    add_grade(data, student_1, "MATH101", 85)
    add_grade(data, student_2, "CS101", 95)
    add_grade(data, student_3, "MATH101", 70)

    save_data(data)
    print("Sample data created successfully.")


if __name__ == "__main__":
    main()