from .models import Student, Course, Enrollment


def get_next_student_id(data):
    """Return the next available student ID."""
    if not data["students"]:
        return 1
    return max(student["id"] for student in data["students"]) + 1


def add_student(data, name):
    """Add a new student and return the new student ID."""
    student_id = get_next_student_id(data)
    student = Student(student_id, name)
    data["students"].append(student.to_dict())
    return student_id


def add_course(data, code, title):
    """Add a new course to the gradebook."""
    for course in data["courses"]:
        if course["code"] == code:
            raise ValueError("Course code already exists.")

    course = Course(code, title)
    data["courses"].append(course.to_dict())


def enroll(data, student_id, course_code):
    """Enroll a student in a course."""
    student_exists = any(student["id"] == student_id for student in data["students"])
    if not student_exists:
        raise ValueError("Student not found.")

    course_exists = any(course["code"] == course_code for course in data["courses"])
    if not course_exists:
        raise ValueError("Course not found.")

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            raise ValueError("Student is already enrolled in this course.")

    enrollment_obj = Enrollment(student_id, course_code)
    data["enrollments"].append(enrollment_obj.to_dict())


def add_grade(data, student_id, course_code, grade):
    """Add a grade to an existing enrollment."""
    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            if not isinstance(grade, (int, float)) or not 0 <= grade <= 100:
                raise ValueError("Grade must be between 0 and 100.")
            enrollment["grades"].append(grade)
            return

    raise ValueError("Enrollment not found.")


def list_students(data, sort_key="name"):
    """Return students sorted by the given key."""
    if sort_key not in ["id", "name"]:
        raise ValueError("Student sort must be 'id' or 'name'.")
    return sorted(data["students"], key=lambda student: student[sort_key])


def list_courses(data, sort_key="code"):
    """Return courses sorted by the given key."""
    if sort_key not in ["code", "title"]:
        raise ValueError("Course sort must be 'code' or 'title'.")
    return sorted(data["courses"], key=lambda course: course[sort_key])


def list_enrollments(data):
    """Return all enrollments sorted by student ID and course code."""
    return sorted(
        data["enrollments"],
        key=lambda enrollment: (enrollment["student_id"], enrollment["course_code"])
    )


def compute_average(data, student_id, course_code):
    """Compute the average grade for a student in a course."""
    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            grades = enrollment["grades"]
            if not grades:
                return 0
            return sum(grades) / len(grades)

    raise ValueError("Enrollment not found.")


def compute_gpa(data, student_id):
    """Compute a student's GPA as the mean of course averages."""
    student_enrollments = [
        enrollment for enrollment in data["enrollments"]
        if enrollment["student_id"] == student_id
    ]

    if not student_enrollments:
        raise ValueError("Student has no enrollments.")

    averages = []
    for enrollment in student_enrollments:
        if enrollment["grades"]:
            averages.append(sum(enrollment["grades"]) / len(enrollment["grades"]))
        else:
            averages.append(0)

    return sum(averages) / len(averages)