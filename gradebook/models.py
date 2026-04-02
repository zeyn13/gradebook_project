class Student:
    """Represents a student."""

    def __init__(self, student_id, name):
        """Initialize a student with an ID and a name."""
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Student id must be a positive integer.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name must be a non-empty string.")

        self.id = student_id
        self.name = name.strip()

    def __str__(self):
        """Return a readable string representation of the student."""
        return f"Student(id={self.id}, name='{self.name}')"

    def to_dict(self):
        """Convert the student object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name
        }


class Course:
    """Represents a course."""

    def __init__(self, code, title):
        """Initialize a course with a code and a title."""
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Course code must be a non-empty string.")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Course title must be a non-empty string.")

        self.code = code.strip()
        self.title = title.strip()

    def __str__(self):
        """Return a readable string representation of the course."""
        return f"Course(code='{self.code}', title='{self.title}')"

    def to_dict(self):
        """Convert the course object to a dictionary."""
        return {
            "code": self.code,
            "title": self.title
        }


class Enrollment:
    """Represents a student's enrollment in a course."""

    def __init__(self, student_id, course_code, grades=None):
        """Initialize an enrollment with student ID, course code, and grades."""
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Student id must be a positive integer.")
        if not isinstance(course_code, str) or not course_code.strip():
            raise ValueError("Course code must be a non-empty string.")

        if grades is None:
            grades = []

        if not isinstance(grades, list):
            raise ValueError("Grades must be a list.")

        for grade in grades:
            if not isinstance(grade, (int, float)) or not 0 <= grade <= 100:
                raise ValueError("Each grade must be numeric and between 0 and 100.")

        self.student_id = student_id
        self.course_code = course_code.strip()
        self.grades = grades

    def __str__(self):
        """Return a readable string representation of the enrollment."""
        return (
            f"Enrollment(student_id={self.student_id}, "
            f"course_code='{self.course_code}', grades={self.grades})"
        )

    def add_grade(self, grade):
        """Add a new grade to the enrollment."""
        if not isinstance(grade, (int, float)) or not 0 <= grade <= 100:
            raise ValueError("Grade must be numeric and between 0 and 100.")
        self.grades.append(grade)

    def average(self):
        """Return the average of all grades in the enrollment."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        """Convert the enrollment object to a dictionary."""
        return {
            "student_id": self.student_id,
            "course_code": self.course_code,
            "grades": self.grades
        }